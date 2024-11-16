from src.todo_service.database.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=True)
    tasks: Mapped[List["Task"]] = relationship(back_populates="user")   # noqa: F821, E501
    is_active: Mapped[bool] = mapped_column(default=False)
