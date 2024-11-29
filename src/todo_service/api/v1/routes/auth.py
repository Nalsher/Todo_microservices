from alembic.util import status
from fastapi import APIRouter, status

from src.todo_service.api.v1.schemas.user_schemas import CreateUserResponse, CreateUserSchema

auth = APIRouter(prefix="/auth")


# @auth.post(path="/register",
#            response_model=CreateUserResponse,
#            summary="Creating User Endpoint",
#            status_code=status.HTTP_200_OK)
# async def create_user(user: CreateUserSchema, service = )