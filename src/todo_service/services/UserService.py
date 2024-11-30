from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response
from fastapi import status

from src.todo_service.database.dtos.UserDTOS import UserRequestDTO
from src.todo_service.database.repositories.AbstractRepositories import RepositoryInterface  # noqa: E501
from src.todo_service.database.utils.Utils import yield_session
from src.todo_service.services.AbstractService import AbstractService


class UserService(AbstractService):

    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    async def create(self, user: UserRequestDTO, session: AsyncSession = Depends(yield_session)) -> Response:  # noqa: E501
        try:
            await self.repository.create(user, session)
            response = Response(content={"Success": "User created successfully"}, status_code=status.HTTP_200_OK)  # noqa: E501
            return response
        except:  # noqa: E722
            response = Response(content={"Failure": "User created failure"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)  # noqa: E501
            return response

    async def get(self, id: int, session: AsyncSession = Depends(yield_session)) -> Response:  # noqa: E501
        try:
            user = self.repository.get(id, session)
            response = Response(content={"Username": user.username, "Email": user.email, "Tasks": user.tasks})   # noqa: E501
            return response
        except:   # noqa: E722
            response = Response(content={"Failure": "User found failure"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)  # noqa: E501
            return response
