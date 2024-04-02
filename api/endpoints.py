from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from core.db import get_db
import crud
from events.base import post_event
import models
import schemas
from src.base62 import encode
from src.utils import clean_encoded_string


router = APIRouter()


@router.post("/urls", response_model=schemas.URL, status_code=status.HTTP_201_CREATED)
async def create_url(
    payload: schemas.URLCreateServer,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
) -> models.URL:
    db_obj = crud.url.get_by_original_url(original_url=str(payload.original_url), db=db)
    if db_obj is not None:
        return db_obj

    db_obj = crud.url.create(obj_in={}, db=db)

    db_obj = crud.url.update(
        db_obj=db_obj,
        obj_in=schemas.URLUpdate(
            original_url=payload.original_url, short_url=encode(db_obj.id)
        ),
        db=db,
    )

    background_tasks.add_task(post_event, event_type="url_created", data=db_obj)

    return db_obj


@router.get("/{short_url}", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
def redirect_original_url(
    short_url: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)
):
    try:
        short_url = clean_encoded_string(short_url)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid URL"
        )

    db_obj = crud.url.get_by_short_url(short_url=clean_encoded_string(short_url), db=db)
    if db_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid URL")

    background_tasks.add_task(post_event, event_type="url_decoded", data=db_obj)

    return RedirectResponse(url=db_obj.original_url)
