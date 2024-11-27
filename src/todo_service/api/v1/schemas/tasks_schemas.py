from datetime import datetime

from pydantic import BaseModel


class CreateTaskSchema(BaseModel):
    title: str
    description: str
    is_active: bool


class UpdateTaskSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    is_active: bool | None = None


class DeleteTaskSchema(BaseModel):
    task_id: int


class TaskSchema(BaseModel):
    task_id: int
    title: str
    description: str
    user_id: int
    is_active: bool


class ResponseTaskSchema(BaseModel):
    task_id: int
    title: str
    description: str
    user_id: int
    is_active: bool
    created_at: datetime
