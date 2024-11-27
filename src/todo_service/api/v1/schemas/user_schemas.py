from pydantic import BaseModel
from typing import List
from src.todo_service.api.v1.schemas.tasks_schemas import TaskSchema


class CreateUserSchema(BaseModel):
    username: str
    password: str
    email: str
    is_active: False


class ResponseUserSchema(BaseModel):
    id: int
    username: str
    email: str
    tasks: List["TaskSchema"]
    is_active: bool


class UpdateUserSchema(BaseModel):
    username: str | None = None
    password: str | None = None
    email: str | None = None
    is_active: False | None = None


class DeleteUserSchema(BaseModel):
    user_id: int
