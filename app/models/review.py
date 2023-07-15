import datetime as dt
from sqlalchemy import BigInteger, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import ENUM


from typing import Optional

from app.models.paper import PaperRevisions
from app.models.user import User
from app.db.base_class import Base


class Review(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    editorID: Mapped[int] = mapped_column(ForeignKey(User.__tablename__ + ".id"))
    associate_editorID: Mapped[int] = mapped_column(ForeignKey(User.__tablename__ + ".id"))
    reviewerID: Mapped[int] = mapped_column(ForeignKey(User.__tablename__ + ".id"))
    revisionID: Mapped[int] = mapped_column(ForeignKey(PaperRevisions.__tablename__ + ".id"))
    process: Mapped[Optional[ENUM]] = mapped_column(
        ENUM(
            "Single Blind",
            "Double Blind",
            name="review_process_enum",
        )
    )

class ReviewComments(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    comment: Mapped[str] = mapped_column(Text)
    comment_datetime: Mapped[dt.date] = mapped_column(DateTime, unique=True)
