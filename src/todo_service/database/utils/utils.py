from os import write

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession
from src.todo_service.config.config import settings


async def create_engine() -> AsyncEngine:
    return create_async_engine(url=settings.database_url, echo=True)

async def session_maker_create() -> AsyncSession:
    engine = await create_engine()

    return async_sessionmaker(bind=engine, expire_on_commit=False)


async def yield_session():
    session_maker = await session_maker_create()

    async with session_maker() as session:
        yield session
