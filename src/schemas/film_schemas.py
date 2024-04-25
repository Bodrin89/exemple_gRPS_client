from pydantic import BaseModel, ConfigDict
from tortoise.contrib.pydantic import pydantic_model_creator

from src.models import FilmModel

FilmSchemaOut_Pydantic = pydantic_model_creator(FilmModel, name='film')


class FilmCreateIn(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: str


class FilmSchemaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str
