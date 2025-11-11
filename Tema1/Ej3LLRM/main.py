
from routers import pelicula, director, auth_users
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(director.router)
app.include_router(pelicula.router)
app.include_router(auth_users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie and Director API"}