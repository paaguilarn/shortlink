from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, HttpUrl
from schemas.types import naive_utcnow


class URLBase(BaseModel):
    original_url: Optional[HttpUrl] = None


class URLCreateServer(URLBase):
    original_url: HttpUrl


class URLCreate(URLBase):
    original_url: Optional[HttpUrl] = None
    short_url: Optional[str] = None
    created_at: Optional[datetime] = Field(default_factory=naive_utcnow)


class URLUpdate(URLBase):
    original_url: Optional[HttpUrl] = None
    short_url: Optional[str] = None


class URLInDBBase(URLBase):
    id: int
    original_url: Optional[HttpUrl] = None
    short_url: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class URL(URLInDBBase):
    pass
