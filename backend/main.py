from fastapi import FastAPI
from v1 import api
from core.models.database import engine
from sqlalchemy import inspect

app = FastAPI()

app.include_router(api.router, prefix='/v1')

@app.get("/")
def hello_world():

    return "Hello, world!"
