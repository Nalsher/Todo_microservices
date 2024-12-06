from src.todo_service.database.dtos.BaseDTOS import BaseResponseDTO, BaseRequestDTO  # noqa: E501
from src.todo_service.database.dtos.UserDTOS import User


class TaskRequestDTO(BaseRequestDTO):
    title: str
    description: str
    user_id: int | None = None
    user: User | None = None
    is_active: bool


class TaskResponseDTO(BaseResponseDTO):
    title: str
    description: str
    is_active: bool


class UpdateTaskRequestDTO(BaseRequestDTO):
    title: str | None = None
    description: str | None = None
    is_active: bool | None = None
