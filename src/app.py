from fastapi import FastAPI

from tasks import api as task_api
from accounts import api as account_api
from auth import auth as auth_api
from other import api as other_api
from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")

templates = Jinja2Templates(directory="../templates")


@app.get("/")
def root():
    return 'Hello, World!'


task_api.init_tasks(app)
account_api.init_accounts(app)
auth_api.init_auth(app)
# other_api.init_other(app)
