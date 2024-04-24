from pydantic import BaseModel, ConfigDict


class AuthIn(BaseModel):
    email: str
    password: str


class AuthOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    access_token: str
    refresh_token: str
