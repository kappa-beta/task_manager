from typing import List

from fastapi import FastAPI, Depends, APIRouter, status, HTTPException

from src.exceptions import EntityConflictError, EntityDoesNotExistError
from src.tasks.schemas import Task as TaskSchema, TaskCreate, TaskUpdate
from src.tasks.services import TaskService

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
