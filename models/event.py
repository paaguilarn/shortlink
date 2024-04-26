import uuid

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String
from sqlalchemy.types import UUID

from core.db import Base
from schemas.types import naive_utcnow


class Event(Base):
    __tablename__ = "event"

    uuid = Column(UUID, primary_key=True, default=uuid.uuid4)
    url_id = Column(BigInteger, ForeignKey("url.id"), nullable=False)
    action = Column(String, nullable=False)
    timestamp = Column(DateTime, default=naive_utcnow)
