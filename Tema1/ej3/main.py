from routers import pelicula, director, auth_director
from fastapi import FastAPI

app = FastAPI()

app.include_router(director.router)
app.include_router(pelicula.router)
app.include_router(auth_director.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie and Director API"}