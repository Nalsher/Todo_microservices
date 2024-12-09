from src.todo_service.database.repositories.TaskRepository import TaskRepository  # noqa: E501
from src.todo_service.database.repositories.UserRepository import UserRepository   # noqa: E501

UserRepo = UserRepository()

TaskRepo = TaskRepository()


async def UserRepoReturn() -> UserRepository:
    return UserRepo


async def TaskRepoReturn() -> TaskRepository:
    return TaskRepo
