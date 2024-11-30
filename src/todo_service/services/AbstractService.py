from abc import ABC, abstractmethod
from src.todo_service.database.repositories.AbstractRepositories import RepositoryInterface  # noqa: E501
from fastapi import Response
from src.todo_service.database.dtos.UserDTOS import UserRequestDTO


class AbstractService(ABC):

    @abstractmethod
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    @abstractmethod
    async def create(self, user: UserRequestDTO) -> Response:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int) -> Response:
        raise NotImplementedError

    @abstractmethod
    async def get(self, *args) -> Response:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, *args) -> Response:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *args) -> Response:
        raise NotImplementedError
