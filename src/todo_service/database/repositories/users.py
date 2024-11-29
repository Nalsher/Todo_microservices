from sqlalchemy.ext.asyncio import AsyncSession
from src.todo_service.database.repositories.AbstractRepositories import RepositoryInterface  # noqa: E501


class UserRepository(RepositoryInterface):

    async def create(self, *args, session: AsyncSession) -> None:
        pass
