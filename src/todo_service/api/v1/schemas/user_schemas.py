from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    username: str
    password: str
    email: str
    tasks: List["Task"] | None = None
    is_active: False


class UpdateUserSchema(BaseModel):
    username: str | None = None
    password: str | None = None
    email: str | None = None
    tasks: List["Task"] | None = None
    is_active: False | None = None


class DeleteUserSchema(BaseModel):
    user_id: int
