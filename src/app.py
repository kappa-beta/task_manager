from fastapi import FastAPI

from tasks import api as task_api

app = FastAPI()


@app.get("/")
def root():
    return 'Hello, World!'


task_api.init_tasks(app)
