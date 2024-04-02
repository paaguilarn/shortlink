from sqlalchemy.orm import Session

import crud
import schemas


def test_create_new_event_for_url(db: Session):
    original_url = "https://url.com"
    short_url = "shorturl"
    url_db_obj = crud.url.create(
        obj_in=schemas.URLCreate(original_url=original_url, short_url=short_url), db=db
    )

    action = "this_did_that"
    event_db_obj = crud.event.create(
        obj_in=schemas.EventCreate(url_id=url_db_obj.id, action=action), db=db
    )

    assert event_db_obj.url_id == url_db_obj.id
    assert event_db_obj.action == action
