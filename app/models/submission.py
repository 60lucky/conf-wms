import datetime as dt
from sqlalchemy import BigInteger, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from typing import Optional

from app.models.conference import Conference
from app.db.base_class import Base


class Submission(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    journals: Mapped[str] = mapped_column(String(255))
    plag_policy: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    sample_paper: Mapped[str] = mapped_column(String(225), unique=True)
    submission_deadline: Mapped[dt.date] = mapped_column(DateTime, unique=True)
    submission_type: Mapped[ENUM] = mapped_column(
        ENUM(
            "Abstract",
            "Full Paper",
            name="submission_type_enum",
        )
    )
    conferenceID: Mapped[int] = mapped_column(ForeignKey(Conference.__tablename__ + ".id"))

    conference: Mapped["Conference"] = relationship("Conference", backref="users")
