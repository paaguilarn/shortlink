from pydantic import HttpUrl
from sqlalchemy.orm import Session

import crud
import schemas


def test_create_new_url(db: Session):
    original_url = "https://url.com"
    short_url = "shorturl"
    db_obj = crud.url.create(
        obj_in=schemas.URLCreate(original_url=original_url, short_url=short_url), db=db
    )

    assert db_obj.original_url == str(HttpUrl(original_url))
    assert db_obj.short_url == short_url


def test_create_new_empty_url(db: Session):
    db_obj = crud.url.create(obj_in={}, db=db)

    assert db_obj.original_url is None
    assert db_obj.short_url is None
