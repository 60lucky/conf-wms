import datetime as dt
from sqlalchemy import BigInteger, String, ForeignKey , DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from typing import Optional


from app.models.conference import ConferenceRoster
from app.models.submission import SubmittedPapers
from app.db.base_class import Base


class Paper(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    paper_name: Mapped[str] = mapped_column(String(225), unique=True)
    authorID: Mapped[int] = mapped_column(ForeignKey(ConferenceRoster.__tablename__ + ".id"))
    abstract: Mapped[str] = mapped_column(String(225), unique=True)
    fullpaper: Mapped[str] = mapped_column(String(225), unique=True)
   

class PaperRevisions(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    paperID: Mapped[int] = mapped_column(ForeignKey(SubmittedPapers.__tablename__ + ".id"))
    revision_no: Mapped[int] = mapped_column(BigInteger)
    revision_link: Mapped[str] = mapped_column(String(225), unique=True)
    revision_date_time: Mapped[DateTime] = mapped_column(DateTime, unique=True)
    submissionID: Mapped[Optional[int]] = mapped_column(BigInteger)


class PaperStatus(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    paperID: Mapped[int] = mapped_column(ForeignKey(Paper.__tablename__ + ".id"))
    is_final_revision: Mapped[bool] = mapped_column(default=False)
    to_publish: Mapped[bool] = mapped_column(default=False)
    presentation_status: Mapped[Optional[ENUM]] = mapped_column(
        ENUM(
            "Accept",
            "Reject",
            "Soft Accept",
            "Soft Reject",
            name="presentation_status_enum",
        )
    )