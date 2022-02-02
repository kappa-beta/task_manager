from fastapi import FastAPI, Depends, APIRouter, status, HTTPException

from src.exceptions import EntityConflictError
from src.tasks.schemas import Task as TaskSchema, TaskCreate
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
