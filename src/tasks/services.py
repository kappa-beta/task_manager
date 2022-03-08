from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, NoResultFound

from src.config import get_settings
from src.database import get_session
from src.exceptions import EntityConflictError, EntityDoesNotExistError
from src.tasks.models import Task, TimeLog
from src.tasks.schemas import TaskCreate, TaskUpdate, TimeLogCreate


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

    def get_task(self, task_id: int) -> Task:
        return self._get_task(task_id)

    def get_tasks(self) -> Task:
        tasks = self.session.execute(
            select(Task)
        ).scalars().all()
        return tasks

    def update_task(self, task_id: int, task_update: TaskUpdate):
        task = self._get_task(task_id)
        # a = task_update.dict()
        # print(a)
        # b = getattr(task, 'header')
        # print(b)
        # print(task)
        for k, v in task_update.dict(exclude_unset=True).items():
            setattr(task, k, v)

        self.session.commit()
        return task

    def _get_task(self, task_id: int) -> Task:
        try:
            task = self.session.execute(
                select(Task)
                    .where(Task.id == task_id)
            ).scalar_one()
            return task
        except NoResultFound:
            raise EntityDoesNotExistError from None


class TimeLogService:
    def __init__(self, session=Depends(get_session), settings=Depends(get_settings)):
        self.session = session
        self.settings = settings

    def create_time_log(self, task_id: int, create_time_log: TimeLogCreate):
        # create_time_log.time_log_id = task_id
        timelog = TimeLog(
            time_log_id=task_id,
            start=create_time_log.start,
            end=create_time_log.end,
        )
        self.session.add(timelog)
        try:
            self.session.commit()
            return timelog
        except IntegrityError:
            raise EntityConflictError from None
