import datetime as dt
from sqlalchemy import BigInteger, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from typing import Optional

from app.models.conference import Conference
from app.models.paper import Paper
from app.db.base_class import Base


class Journal(Base):
    pass

class JournalSubmission(Base):
    pass