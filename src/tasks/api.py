from typing import List

from fastapi import FastAPI, Depends, APIRouter, status, HTTPException, Request

from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from src.exceptions import EntityConflictError, EntityDoesNotExistError
from src.tasks.schemas import TimeLog as TimeLogSchema, TimeLogCreate, TimeLogUpdate
from src.tasks.schemas import Task as TaskSchema, TaskCreate, TaskUpdate
from src.tasks.services import TaskService, TimeLogService

templates = Jinja2Templates(directory="../templates")


router = APIRouter(
    prefix='/tasks',
)


def init_tasks(app: FastAPI):
    app.include_router(router)


@router.post(
    '',
    response_model=TaskSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
        task_create: TaskCreate,
        service: TaskService = Depends(),
):
    try:
        task = service.create_task(task_create)
    except EntityConflictError:
        raise HTTPException(status.HTTP_409_CONFLICT) from None
    return task


@router.get('/{task_id}', response_model=TaskSchema)
def get_task(
        task_id: int,
        service: TaskService = Depends(),
):
    try:
        return service.get_task(task_id)
    except EntityDoesNotExistError:
        raise HTTPException(status.HTTP_404_NOT_FOUND) from None


@router.get('', response_model=List[TaskSchema])
def get_tasks(
        service: TaskService = Depends(),
):
    try:
        return service.get_tasks()
    except EntityDoesNotExistError:
        raise HTTPException(status.HTTP_404_NOT_FOUND) from None


@router.patch('/{task_id}', response_model=TaskSchema)
def edit_task(
        task_id: int,
        task_update: TaskUpdate,
        service: TaskService = Depends(),
):
    try:
        task = service.update_task(task_id, task_update)
        return task
    except EntityDoesNotExistError:
        raise HTTPException(status.HTTP_404_NOT_FOUND) from None


@router.post(
    '/{task_id}/time_log',
    response_model=TimeLogSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_time_log(
        task_id: int,
        time_log_create: TimeLogCreate,
        service: TimeLogService = Depends(),
):
    try:
        time_log = service.create_time_log(task_id, time_log_create)
    except EntityConflictError:
        raise HTTPException(status.HTTP_409_CONFLICT) from None
    return time_log


@router.get(
    '/{task_id}/time_logs',
    response_model=List[TimeLogSchema],
)
def get_time_logs(
        task_id: int,
        service: TimeLogService = Depends(),
):
    try:
        return service.get_time_logs(task_id)
    except EntityDoesNotExistError:
        raise HTTPException(status.HTTP_404_NOT_FOUND) from None


@router.patch(
    '/{task_id}/time_logs',
    response_model=TimeLogSchema,
)
def edit_time_log(
        task_id: int,
        time_log_update: TimeLogUpdate,
        service: TimeLogService = Depends(),
):
    try:
        time_log = service.update_time_log(task_id, time_log_update)
        return time_log
    except EntityDoesNotExistError:
        raise HTTPException(status.HTTP_404_NOT_FOUND) from None


@router.get(
    '/task_create',
    response_class=HTMLResponse,
)
def read_create_task(request: Request):
    return templates.TemplateResponse("task_create.html", {"request": request})
