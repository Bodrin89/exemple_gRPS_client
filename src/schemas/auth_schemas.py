from pydantic import BaseModel, ConfigDict, EmailStr


class AuthIn(BaseModel):
    email: EmailStr
    password: str


class AuthOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    access_token: str
    refresh_token: str
