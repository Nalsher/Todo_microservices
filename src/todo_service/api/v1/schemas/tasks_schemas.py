from pydantic import BaseModel


class CreateTaskSchema(BaseModel):
    title: str
    description: str
    user_id: int | None = None
    user: User | None = None
    is_active: bool


class CreateTaskSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    user_id: int | None = None
    user: User | None = None
    is_active: bool | None = None


class DeleteTaskSchema(BaseModel):
    task_id: int

