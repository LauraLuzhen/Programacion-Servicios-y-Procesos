# pip install pyjwt
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db.client import db_client
from db.schemas.director import director_schema, directors_schema  
from db.models.director import Director  

router = APIRouter(prefix="/directors_db", tags=["directors_db"])

# GET todos los directores
@router.get("/", response_model=list[Director])
async def directors():
    return directors_schema(db_client.ej3.directors.find())

# GET director por query id
@router.get("", response_model=Director)
async def director(id: str):
    return search_director_id(id)

# GET director por path id
@router.get("/{id}", response_model=Director)
async def director(id: str):
    return search_director_id(id)

# POST añadir director
@router.post("/", response_model=Director, status_code=201)
async def add_director(director: Director):
    if type(search_director(director.nombre, director.apellidos)) == Director:
        raise HTTPException(status_code=409, detail="Director ya existe")
    
    director_dict = director.model_dump()
    del director_dict["id"]
    id = db_client.ej3.directors.insert_one(director_dict).inserted_id
    director_dict["id"] = str(id)
    return Director(**director_dict)

# PUT modificar director
@router.put("/{id}", response_model=Director)
async def modify_director(id: str, new_director: Director):
    director_dict = new_director.model_dump()
    del director_dict["id"]
    try:
        db_client.ej3.directors.find_one_and_replace({"_id": ObjectId(id)}, director_dict)
        return search_director_id(id)
    except:
        raise HTTPException(status_code=404, detail="Director no encontrado")

# DELETE director
@router.delete("/{id}", response_model=Director)
async def delete_director(id: str):
    found = db_client.ej3.directors.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        raise HTTPException(status_code=404, detail="Director no encontrado")
    return Director(**director_schema(found))

# Función auxiliar para buscar director por id
def search_director_id(id: str):
    try:
        director = director_schema(db_client.ej3.directors.find_one({"_id": ObjectId(id)}))
        return Director(**director)
    except:
        return {"Error": "Director no encontrado"}

# Función auxiliar para buscar director por nombre y apellido
def search_director(nombre: str, apellido: str):
    try:
        director = director_schema(db_client.ej3.directors.find_one({"nombre": nombre, "apellido": apellido}))
        return Director(**director)
    except:
        return {"Error": "Director no encontrado"}


