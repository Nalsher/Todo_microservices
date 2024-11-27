from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository:

    async def create_user(self, session: AsyncSession, user_model):
        pass
