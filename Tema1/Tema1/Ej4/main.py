from fastapi import FastAPI
from routers import profesor, asignatura

app = FastAPI()

# Routers
app.include_router(profesor.router, prefix="/profesor", tags=["Profesor"])
app.include_router(asignatura.router, prefix="/asignatura", tags=["Asignatura"])

@app.get("/")
def root():
    return {"message": "Welcome to the Educational API"}