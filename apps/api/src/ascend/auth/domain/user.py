from typing import NewType
from uuid import UUID
from pydantic import BaseModel, EmailStr

UserId = NewType("UserId", UUID)


class User(BaseModel):
    id: UserId
    email: EmailStr

    class Config:
        orm_mode = True
