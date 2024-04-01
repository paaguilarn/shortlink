from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

from core.config import settings


engine = create_engine(str(settings.db_uri))


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


Base = declarative_base()
