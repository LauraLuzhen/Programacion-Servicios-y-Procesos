from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from .auth_users import auth_user
from db.client import db_client
from db.models.user import User
from db.schemas.user import user_schema, users_schema

router = APIRouter(prefix="/usersdb", tags=["usersdb"])

# ==========================
# RUTAS PROTEGIDAS CON JWT
# ==========================

@router.get("/", response_model=list[User])
async def users(current_user: User = Depends(auth_user)):
    """Devuelve todos los usuarios de la base de datos"""
    return users_schema(db_client.test.users.find())

@router.get("", response_model=User)
async def user(id: str, current_user: User = Depends(auth_user)):
    return search_user_id(id)

@router.get("/{id}", response_model=User)
async def user_by_id(id: str, current_user: User = Depends(auth_user)):
    return search_user_id(id)

@router.post("/", response_model=User, status_code=201)
async def add_user(user: User, current_user: User = Depends(auth_user)):
    if isinstance(search_user(user.name, user.surname), User):
        raise HTTPException(status_code=409, detail="User already exists")

    user_dict = user.model_dump()
    del user_dict["id"]
    id = db_client.test.users.insert_one(user_dict).inserted_id
    user_dict["id"] = str(id)
    return User(**user_dict)

@router.put("/{id}", response_model=User)
async def modify_user(id: str, new_user: User, current_user: User = Depends(auth_user)):
    user_dict = new_user.model_dump()
    del user_dict["id"]
    try:
        db_client.test.users.find_one_and_replace({"_id": ObjectId(id)}, user_dict)
        return search_user_id(id)
    except:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{id}", response_model=User)
async def delete_user(id: str, current_user: User = Depends(auth_user)):
    found = db_client.test.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**user_schema(found))

# ==========================
# FUNCIONES AUXILIARES
# ==========================

def search_user_id(id: str):
    try:
        user = user_schema(db_client.test.users.find_one({"_id": ObjectId(id)}))
        return User(**user)
    except:
        raise HTTPException(status_code=404, detail="User not found")

def search_user(name: str, surname: str):
    try:
        user = user_schema(db_client.test.users.find_one({"name": name, "surname": surname}))
        return User(**user)
    except:
        return None
