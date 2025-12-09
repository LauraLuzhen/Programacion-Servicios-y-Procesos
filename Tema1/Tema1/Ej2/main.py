from fastapi import FastAPI
from routers import autor, libro
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(autor.router)
app.include_router(libro.router)

@app.get("/")
def root():
    return {"Mensaje" : "API de autor y libro"}