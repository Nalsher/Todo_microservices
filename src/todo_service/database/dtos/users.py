from src.todo_service.database.dtos.base import BaseDTO, BaseResponseDTO, BaseRequestDTO  # noqa: E501
from typing import List


class UserRequestDTO(BaseRequestDTO):
    username: str
    password: str
    email: str
    is_active: False


class UserUpdateDTO(BaseRequestDTO):
    username: str | None = None
    password: str | None = None
    email: str | None = None
    is_active: False | None = None


class UserResponseDTO(BaseResponseDTO):
    username: str
    password: str
    email: str
    is_active: bool


class ListUserResponse:
    users: List[UserResponseDTO]


class User(BaseDTO):
    username: str
    password: str
    email: str
    is_active: bool
