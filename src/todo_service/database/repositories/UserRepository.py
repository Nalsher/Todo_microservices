from typing import Any, List

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.todo_service.database.repositories.AbstractRepositories import RepositoryInterface  # noqa: E501
from src.todo_service.database.utils.Utils import yield_session
from src.todo_service.database.dtos.UserDTOS import UserRequestDTO, UserUpdateDTO  # noqa: E501
from src.todo_service.database.models.users import User
from sqlalchemy import select


class UserRepository(RepositoryInterface):

    async def create(self, user: UserRequestDTO, session: AsyncSession = Depends(yield_session)) -> None:  # noqa: E501
        async with session as _session:
            new_user = User(username=user.username, password=user.password,
                            email=user.email, is_active=False)
            _session.add(new_user)
            await _session.commit()

    async def delete(self, id: int, session: AsyncSession = Depends(yield_session)) -> bool:   # noqa: E501
        async with session as _session:
            try:
                user = await _session.get(User, id)
                await _session.delete(user)
                await _session.commit()
                return True
            except:     # noqa: E722
                return False

    async def get(self, id: int, session: AsyncSession = Depends(yield_session)) -> Any:   # noqa: E501
        async with session as _session:
            try:
                user = await _session.get(User, id)
                return user
            except:     # noqa: E722
                raise Exception("Not Found User")

    async def get_all(self, session: AsyncSession = Depends(yield_session)) -> List[Any]:   # noqa: E501
        async with session as _session:
            try:
                query = select(User)
                execute = await _session.execute(query)
                result = execute.scalars().all()
                return result
            except:     # noqa: E722
                raise Exception("Error get all")

    async def update(self, user_id: int, user: UserUpdateDTO, session: AsyncSession = Depends(yield_session)) -> bool:   # noqa: E501
        async with session as _session:
            user_get = await _session.get(User, user_id)
            if user.username:
                user_get.username = user.username
            if user.password:
                user_get.password = user.password
            if user.email:
                user_get.email = user.email
            if user.is_active:
                user_get.is_active = user.is_active
            await _session.commit()
