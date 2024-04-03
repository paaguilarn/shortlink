from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from schemas.types import naive_utcnow


class EventBase(BaseModel):
    url_id: Optional[int] = None
    action: Optional[str] = None


class EventCreate(EventBase):
    url_id: int
    action: str
    timestamp: Optional[datetime] = Field(default_factory=naive_utcnow)


class EventInDBBase(EventBase):
    id: int
    url_id: int
    action: int
    timestamp: datetime


class Event(EventInDBBase):
    pass
