from sqlalchemy import BigInteger, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import ENUM


from typing import Optional

from app.models.paper import PaperRevisions
from app.models.conference import ConferenceEditors
from app.models.conference import ConferenceAssociateEditors
from app.models.conference import ConferenceReviewer
from app.db.base_class import Base


class Review(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    editor_id: Mapped[int] = mapped_column(ForeignKey(ConferenceEditors.__tablename__ + ".id"))
    associate_editor_id: Mapped[int] = mapped_column(ForeignKey(ConferenceAssociateEditors.__tablename__ + ".id"))
    reviewer_id: Mapped[int] = mapped_column(ForeignKey(ConferenceReviewer.__tablename__ + ".id"))
    revision_id: Mapped[int] = mapped_column(ForeignKey(PaperRevisions.__tablename__ + ".id"))
    process: Mapped[Optional[ENUM]] = mapped_column(
        ENUM(
            "Single Blind",
            "Double Blind",
            name="review_process_enum",
        )
    )

class ReviewComments(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    review_id: Mapped[int] = mapped_column(ForeignKey(Review.__tablename__ + ".id"))
    comment: Mapped[str] = mapped_column(Text)
    comment_datetime: Mapped[DateTime] = mapped_column(DateTime, unique=True)
