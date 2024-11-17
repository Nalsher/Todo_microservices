from pydantic import BaseModel


class BaseDTO(BaseModel):
    pass


class BaseResponseDTO(BaseDTO):
    pass


class BaseRequestDTO(BaseDTO):
    pass