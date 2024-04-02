from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
import schemas


def create(obj_in: schemas.URLCreate, db: Session) -> models.URL:
    db_obj = models.URL(**jsonable_encoder(obj_in, exclude_none=True))
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj


def get_by_short_url(short_url: str, db: Session) -> models.URL:
    stmt = select(models.URL).where(models.URL.short_url == short_url)

    return db.scalars(stmt).first()


def get_by_original_url(original_url: str, db: Session) -> models.URL:
    stmt = select(models.URL).where(models.URL.original_url == original_url)

    return db.scalars(stmt).first()


def update(db_obj: models.URL, obj_in: schemas.URLUpdate, db: Session) -> models.URL:
    data = jsonable_encoder(obj_in, exclude_none=True)
    for field in data:
        if hasattr(db_obj, field):
            setattr(db_obj, field, data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
