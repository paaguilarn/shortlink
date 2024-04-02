from sqlalchemy.orm import Session

from core.db import engine
import crud
import models
import schemas
from events.base import subscribe


def handle_url_created_event(url: models.URL):
    with Session(engine) as db:
        crud.event.create(
            obj_in=schemas.EventCreate(url_id=url.id, action="url_created"), db=db
        )


def handle_url_decoded_event(url: models.URL):
    with Session(engine) as db:
        crud.event.create(
            obj_in=schemas.EventCreate(url_id=url.id, action="url_decoded"), db=db
        )


def setup_usage_tracking_handlers():
    subscribe("url_created", handle_url_created_event)
    subscribe("url_decoded", handle_url_decoded_event)
