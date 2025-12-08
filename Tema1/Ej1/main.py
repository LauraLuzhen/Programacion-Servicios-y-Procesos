# main.py - Laura Luzhen Rodríguez Morán

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Routers
from routers import director, supermercado, auth_users, users_db

app = FastAPI()

# Asegúrate de que la carpeta "static" existe si la montas
app.mount("/static", StaticFiles(directory="static"), name="static")

# Primero el router de auth (login/register), luego usersdb y finalmente tus recursos
app.include_router(auth_users.router)   # expone /login, /register, /auth/me según tu auth_users.py
app.include_router(users_db.router)      # expone /usersdb...
app.include_router(director.router)     # expone /directors...
app.include_router(supermercado.router) # expone /supermarkets...

@app.get("/")
def root():
    return {"Mensaje": "API de director y supermercado"}
