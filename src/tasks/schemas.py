from typing import Optional

from fastapi import UploadFile
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    header: str
    description: str
    first_name: Optional[str]
    last_name: Optional[str]
    avatar: Optional[str]

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    email: str
    username: str
    password: str


class TaskUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
