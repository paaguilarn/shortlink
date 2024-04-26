from sqlalchemy import BigInteger, Column, DateTime, String

from core.db import Base
from schemas.types import naive_utcnow


class URL(Base):
    __tablename__ = "url"

    id = Column(BigInteger, primary_key=True)
    original_url = Column(String)
    short_url = Column(String(8))
    created_at = Column(DateTime, default=naive_utcnow)
