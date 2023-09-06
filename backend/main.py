from fastapi import FastAPI
from v1 import api

app = FastAPI()

app.include_router(api.router, prefix='/v1')
