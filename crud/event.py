from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import models
import schemas


def create(obj_in: schemas.EventCreate, db: Session) -> models.URL:
    db_obj = models.Event(**jsonable_encoder(obj_in, exclude_none=True))
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
