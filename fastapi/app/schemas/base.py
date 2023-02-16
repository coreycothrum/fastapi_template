from typing import Optional

from pydantic import BaseModel as pydanticBaseModel


class BaseModel(pydanticBaseModel):
    pass


class ORMBaseModel(BaseModel):
    id: Optional[int] = None

    class Config:
        orm_mode = True
