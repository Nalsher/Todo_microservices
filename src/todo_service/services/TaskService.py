from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response

from src.todo_service.api.v1.schemas.TaskSchemas import CreateTaskSchema
from src.todo_service.database.repositories.AbstractRepositories import RepositoryInterface  # noqa: E501
from src.todo_service.database.utils.Utils import yield_session
from src.todo_service.services.AbstractService import AbstractService


class TaskService(AbstractService):

    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    async def create(self, entity: CreateTaskSchema, session: AsyncSession = Depends(yield_session)) -> Response:  # noqa: E501
        await self.repository.create(entity, session)

    async def delete(self, id: int, session: AsyncSession = Depends(yield_session)) -> Response:  # noqa: E501
        await self.repository.delete(id, session)
