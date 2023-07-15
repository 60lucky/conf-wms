from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from typing import Optional

from app.models.conference import Conference
from app.models.user import User
from app.db.base_class import Base


class ConferenceEditorsReviewers(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    conferenceID: Mapped[int] = mapped_column(ForeignKey(Conference.__tablename__ + ".id"))
    editorID: Mapped[int] = mapped_column(ForeignKey(User.__tablename__ + ".id"))
    associate_editorID: Mapped[int] = mapped_column(ForeignKey(User.__tablename__ + ".id"))
    reviewerID: Mapped[int] = mapped_column(ForeignKey(User.__tablename__ + ".id"))

    user: Mapped["User"] = relationship("User", backref="users")
    conference: Mapped["Conference"] = relationship("Conference", backref="users")