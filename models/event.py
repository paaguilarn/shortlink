from sqlalchemy import Column, Integer, DateTime, ForeignKey, String

from core.db import Base


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, ForeignKey("url.id"), nullable=False)
    action = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
