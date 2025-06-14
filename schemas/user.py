from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    id: str
    name: str
    email: EmailStr
    is_active: bool = True


class UserCreate(BaseModel):
    name: str
    email: EmailStr

class Users(BaseModel):
    users: list[User]


class Response(BaseModel):
    message: Optional[str] = None
    data: Optional[User | Users] = None




