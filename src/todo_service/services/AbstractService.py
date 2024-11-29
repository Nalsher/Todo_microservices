from abc import ABC, abstractmethod


class AbstractService(ABC):

    @abstractmethod
    def __init__(self, repository):
        self.repository = repository
