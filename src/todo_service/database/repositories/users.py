from sqlalchemy.ext.asyncio import AsyncSession
from src.todo_service.database.repositories.AbstractRepositories import RepositoryInterface

class UserRepository(RepositoryInterface):

    async def create(self, *args) -> None:
        pass
