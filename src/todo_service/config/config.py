import os
from dotenv import load_dotenv

load_dotenv()


class Settings_Config:

    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_PORT = os.getenv("POSTGRES_PORT")
    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB_NAME = os.getenv("POSTGRES_DB")

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"   # noqa: E501


settings = Settings_Config()
