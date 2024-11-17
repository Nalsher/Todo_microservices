from src.todo_service.database.dtos.base import BaseDTO, BaseResponseDTO, BaseRequestDTO
from typing import List


class UserRequestDTO(BaseRequestDTO):
    username: str
    password: str
    email: str
    tasks: List["Task"] | None = None
    is_active: False


class UserResponseDTO(BaseResponseDTO):
    username: str
    password: str
    email: str
    tasks: List["Task"] | None = None
    is_active: bool


class ListUserResponse:
    users: List[UserResponseDTO]


class User(BaseDTO):
    username: str
    password: str
    email: str
    tasks: List["Task"] | None = None
    is_active: bool