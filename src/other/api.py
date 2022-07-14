from fastapi import FastAPI, APIRouter, Request

from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

# templates = Jinja2Templates(directory="../templates")
# templates = Jinja2Templates(directory="././templates")
templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix='/other',
)


def init_other(app: FastAPI):
    app.include_router(router)


@router.get(
    '/task_create',
    response_class=HTMLResponse,
)
def read_create_task(request: Request):
    return templates.TemplateResponse("task_create.html", {"request": request})
