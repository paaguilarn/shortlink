from typing import Generator

import pytest
from sqlalchemy import delete
from sqlalchemy.orm import Session

from core.db import engine
import models


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        delete(models.URL)
        session.commit()
