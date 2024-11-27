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
