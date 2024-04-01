from datetime import datetime

from sqlalchemy import DateTime, Column, Integer, String, Text

from core.db import Base


class URL(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True)
    original_url = Column(String)
    short_url = Column(String(8))
    created_at = Column(DateTime, default=datetime.utcnow)
