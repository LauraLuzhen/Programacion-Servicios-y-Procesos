from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad User
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [
    User(id=1, name="Alice", surname="Smith", age=28),
    User(id=2, name="Bob", surname="Johnson", age=35),
    User(id=3, name="Charlie", surname="Brown", age=22)
]

@app.get("/users")
def users():
    return users_list

@app.get("/users/{user_id}")
def user(user_id: int):
    # users = filter(lambda user: user.id == user_id, users_list)
    users = [user for user in users_list if user.id == user_id]
    if len(users) != 0:
        return users
    else:
        return {"error": "User not found"}

