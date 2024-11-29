from abc import ABC, abstractmethod
from typing import Any, List


class RepositoryInterface(ABC):

    @abstractmethod
    async def create(self, *args) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List[Any]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *args) -> bool:
        raise NotImplementedError
