# Laura Luzhen Rodríguez Morán

from fastapi import FastAPI
from routers import director

app = FastAPI()

app.include_router(director.router)

