from fastapi import FastAPI
from routers import colegios, alumnos, auth_users

app = FastAPI()

# Routers
app.include_router(colegios.router)
app.include_router(alumnos.router)
app.include_router(auth_users.router)

@app.get("/")
def root():
    return {"Hello": "World"}