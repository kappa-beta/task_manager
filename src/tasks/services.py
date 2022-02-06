from fastapi import Depends
from sqlalchemy.exc import IntegrityError

from src.config import get_settings
from src.database import get_session
from src.exceptions import EntityConflictError
from src.tasks.models import Task
from src.tasks.schemas import TaskCreate


class TaskService:
    def __init__(self, session=Depends(get_session), settings=Depends(get_settings)):
        self.session = session
        self.settings = settings

    def create_task(self, task_create: TaskCreate):
        task = Task(
            header=task_create.header,
            description=task_create.description,
            plan_start=task_create.plan_start,
            plan_end=task_create.plan_end,
            executors=task_create.executors,
        )
        self.session.add(task)
        try:
            self.session.commit()
            return task
        except IntegrityError:
            raise EntityConflictError from None
