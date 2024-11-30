from abc import ABC, abstractmethod
from src.todo_service.database.repositories.AbstractRepositories import RepositoryInterface
from fastapi import Response


class AbstractService(ABC):

    @abstractmethod
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    @abstractmethod
    def create(self, *args) -> Response:
        self.repository.create(*args)

    @abstractmethod
    def delete(self, id: int) -> Response:
        self.repository.delete(id)

    @abstractmethod
    def get(self, *args) -> Response:
        self.repository.get(*args)
