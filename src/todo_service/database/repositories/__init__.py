from sqlalchemy.ext.asyncio import AsyncSession

from src.todo_service.database.utils.utils import yield_session
from src.todo_service.database.models.users import User


class UserRepository:

    async def create_user(self, session: AsyncSession, user_model):
        pass