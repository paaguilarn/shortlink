from typing import Generator

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import delete
from sqlalchemy.orm import Session

from api.main import app
from core.db import engine
import models


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        session.execute(delete(models.Event))
        session.execute(delete(models.URL))
        session.commit()


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def url_sample(db: Session):
    url = models.URL(original_url="https://another-url.com", short_url="XYZ")
    db.add(url)
    db.commit()
    db.refresh(url)

    return url
