from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, func

from src.todo_service.database.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Task(Base):
    __tablename__ = "tasks"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="tasks")  # noqa: F821
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())  # noqa: E501
    is_active: Mapped[bool] = mapped_column(default=False)
