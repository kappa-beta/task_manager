from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    header: str
    description: Optional[str]
    plan_start: Optional[str]
    plan_end: Optional[str]
    executors: Optional[str]

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    header: str
    description: Optional[str] = None
    plan_start: Optional[str] = None
    plan_end: Optional[str] = None
    executors: Optional[str] = None


class TaskUpdate(BaseModel):
    header: Optional[str] = None
    description: Optional[str] = None
    plan_start: Optional[str] = None
    plan_end: Optional[str] = None
    executors: Optional[str] = None
