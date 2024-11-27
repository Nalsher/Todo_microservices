from fastapi import FastAPI


def create_app() -> FastAPI:
    _app = FastAPI(title="ToDo_Service", description="Backend microservice of todolist",   # noqa: E501
                   version="0.1.0", docs_url="/",
                   redoc_url="/docs")

    return _app


app = create_app()
