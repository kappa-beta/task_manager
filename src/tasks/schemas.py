from typing import Optional, List
from datetime import date

from pydantic import BaseModel


class TimeLog(BaseModel):
    id: int
    time_log_id: int
    start: date
    end: Optional[date]

    class Config:
        orm_mode = True


class Task(BaseModel):
    id: int
    header: str
    description: Optional[str]
    plan_start: Optional[date]
    plan_end: Optional[date]
    executors: Optional[str]
    time_log: Optional[List[TimeLog]]

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    header: str
    description: Optional[str] = None
    plan_start: Optional[date] = None
    plan_end: Optional[date] = None
    executors: Optional[str] = None


class TaskUpdate(BaseModel):
    header: Optional[str] = None
    description: Optional[str] = None
    plan_start: Optional[date] = None
    plan_end: Optional[date] = None
    executors: Optional[str] = None


# class TimeLog(BaseModel):
#     id: int
#     time_log_id: int
#     start: date
#     end: Optional[date]
#
#     class Config:
#         orm_mode = True


class TimeLogCreate(BaseModel):
    # time_log_id: int
    start: date
    end: Optional[date]


class TimeLogUpdate(BaseModel):
    start: date | None = None
    end: date
