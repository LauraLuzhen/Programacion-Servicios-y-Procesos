# pip install pyjwt
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db.client import db_client
from db.schemas.pelicula import pelicula_schema, peliculas_schema  
from db.models.pelicula import Pelicula  

router = APIRouter(prefix="/peliculas_db", tags=["peliculass_db"])

# GET todas las peliculas
@router.get("/", response_model=list[Pelicula])
async def peliculas():
    return peliculas_schema(db_client.ej3.peliculas.find())

# GET pelicula por query id
@router.get("", response_model=Pelicula)
async def pelicula(id: str):
    return search_pelicula_id(id)

# GET pelicula por path id
@router.get("/{id}", response_model=Pelicula)
async def pelicula(id: str):
    return search_pelicula_id(id)

# POST añadir pelicula
@router.post("/", response_model=Pelicula, status_code=201)
async def add_pelicula(pelicula: Pelicula):
    if type(search_pelicula(pelicula.titulo.elicula)) == Pelicula:
        raise HTTPException(status_code=409, detail="Pelicula ya existe")
    
    pelicula_dict = pelicula.model_dump()
    del pelicula_dict["id"]
    id = db_client.ej3.peliculas.insert_one(pelicula_dict).inserted_id
    pelicula_dict["id"] = str(id)
    return Pelicula(**pelicula_dict)

# PUT modificar pelicula
@router.put("/{id}", response_model=Pelicula)
async def modify_pelicula(id: str, new_pelicula: Pelicula):
    pelicula_dict = new_pelicula.model_dump()
    del pelicula_dict["id"]
    try:
        db_client.ej3.peliculas.find_one_and_replace({"_id": ObjectId(id)}, pelicula_dict)
        return search_pelicula_id(id)
    except:
        raise HTTPException(status_code=404, detail="Pelicula no encontrado")

# DELETE pelicula
@router.delete("/{id}", response_model=Pelicula)
async def delete_pelicula(id: str):
    found = db_client.ej3.peliculas.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        raise HTTPException(status_code=404, detail="Pelicula no encontrado")
    return Pelicula(**pelicula_schema(found))

# Función auxiliar para buscar pelicula por id
def search_pelicula_id(id: str):
    try:
        pelicula = pelicula_schema(db_client.ej3.peliculas.find_one({"_id": ObjectId(id)}))
        return Pelicula(**pelicula)
    except:
        return {"Error": "Pelicula no encontrado"}

# Función auxiliar para buscar pelicula por el titulo
def search_pelicula(nombre: str, apellido: str):
    try:
        pelicula = pelicula_schema(db_client.ej3.peliculas.find_one({"nombre": nombre, "apellido": apellido}))
        return Pelicula(**pelicula)
    except:
        return {"Error": "Pelicula no encontrado"}


