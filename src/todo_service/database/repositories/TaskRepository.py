from typing import Any, List

from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.todo_service.database.dtos.TaskDTOS import TaskRequestDTO
from src.todo_service.database.repositories.AbstractRepositories import RepositoryInterface   # noqa: E501
from src.todo_service.database.utils.Utils import yield_session
from src.todo_service.database.models.tasks import Task


class TaskRepository(RepositoryInterface):

    async def create(self, task: TaskRequestDTO, session: AsyncSession = Depends(yield_session)) -> None:   # noqa: E501
        async with session as _session:
            new_task = Task(title=task.title, description=task.description,
                            user_id=task.user_id, user=task.user,
                            is_active=False)
            _session.add(new_task)
            await _session.commit()

    async def get(self, task_id: int, session: AsyncSession = Depends(yield_session)) -> Any:   # noqa: E501
        async with session as _session:
            get_task = await _session.get(Task, task_id)
            return get_task

    async def delete(self, id: int, session: AsyncSession = Depends(yield_session)) -> bool:   # noqa: E501
        async with session as _session:
            delete = await _session.get(Task, id)
            await _session.delete(delete)
            await _session.commit()
            return True

    async def get_all(self, session: AsyncSession = Depends(yield_session)) -> List[Any]:   # noqa: E501
        async with session as _session:
            query = select(Task)
            execute = await _session.execute(query)
            results = execute.scalars().all()
            return results

    async def update(self, *args) -> bool:
        pass
