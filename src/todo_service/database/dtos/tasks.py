from src.todo_service.database.dtos.base import BaseDTO, BaseResponseDTO, BaseRequestDTO
from src.todo_service.database.dtos.users import User
from typing import List


class TaskRequestDTO(BaseRequestDTO):
    title: str
    description: str
    user_id: int | None = None
    user: User | None = None
    is_active: bool


class TaskResponseDTO(BaseResponseDTO):
    pass