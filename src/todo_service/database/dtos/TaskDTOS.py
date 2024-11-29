from src.todo_service.database.dtos.BaseDTOS import BaseResponseDTO, BaseRequestDTO
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
