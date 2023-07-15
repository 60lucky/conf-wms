from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from typing import Optional

from app.models.conference import Conference
from app.models.user import User
from app.db.base_class import Base


class Paper(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    paper_name: Mapped[str] = mapped_column(String(225), unique=True)
    authorID: Mapped[int] = mapped_column(ForeignKey(User.__tablename__ + ".id"))
    abstract: 
    fullpaper: 
   
    user: Mapped["User"] = relationship("User", backref="users")
    conference: Mapped["Conference"] = relationship("Conference", backref="users")