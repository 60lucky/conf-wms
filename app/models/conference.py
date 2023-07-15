from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from typing import Optional


from app.models.user import User
from app.db.base_class import Base


class Conference(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    conference_theme: Mapped[str] = mapped_column(String(255))
    in_charge: Mapped[int] = mapped_column(ForeignKey(User.__tablename__ + ".id"))
    conference_track: Mapped[str] = mapped_column(String(225), unique=True)
    chair_name: Mapped[str] = mapped_column(String(225), unique=True)
    chair_designation: Mapped[str] = mapped_column(String(225), unique=True)
    co_chair_name: Mapped[str] = mapped_column(String(225), unique=True)
    chair_designation: Mapped[str] = mapped_column(String(225), unique=True)
    conference_board: Mapped[str] = mapped_column(String(225), unique=True)
    organizing_committee: Mapped[str] = mapped_column(String(225), unique=True)
    international_advisory_board: Mapped[str] = mapped_column(String(225), unique=True)
    editor: Mapped[int] = mapped_column(ForeignKey(User.__tablename__ + ".id"))

    user: Mapped["User"] = relationship("User", backref="users")
