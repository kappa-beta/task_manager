from fastapi import FastAPI
from tasks import api as task_api
from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")
# templates = Jinja2Templates(directory="./templates")


@app.get("/")
def root():
    return 'Hello, World!'


task_api.init_tasks(app)
