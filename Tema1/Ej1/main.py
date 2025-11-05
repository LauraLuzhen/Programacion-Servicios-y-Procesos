# Laura Luzhen Rodríguez Morán

from fastapi import FastAPI
from routers import director, supermercado
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(director.router)
app.include_router(supermercado.router)

@app.get("/")
def root():
    return {"Mensaje": "API de director y supermercado"}