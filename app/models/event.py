from sqlalchemy import BigInteger, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from typing import Optional

from app.models.conference import Conference
from app.db.base_class import Base


class Event(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    venue: Mapped[str] = mapped_column(Text)
    reg_open: Mapped[DateTime] = mapped_column(DateTime, unique=True)
    reg_close: Mapped[DateTime] = mapped_column(DateTime, unique=True)
    event_start: Mapped[DateTime] = mapped_column(DateTime, unique=True) 
    event_end: Mapped[str] = mapped_column(Text)
    max_participants: Mapped[int] = mapped_column(BigInteger)
    conferenceID: Mapped[int] = mapped_column(ForeignKey(Conference.__tablename__ + ".id"))

