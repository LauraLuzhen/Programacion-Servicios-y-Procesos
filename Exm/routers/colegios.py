from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db.client import db_client
from db.schemas.colegios import colegio_schema, colegios_schema  
from db.models.colegios import Colegio  
from db.models.alumnos import Alumno  
from db.schemas.alumnos import alumnos_schema  

router = APIRouter(prefix="/colegios_db", tags=["colegios_db"])

# GET todos los colegios
@router.get("/", response_model=list[Colegio])
async def colegios():
    return colegios_schema(db_client.colegios.exm.find())

# GET colegio por path id
@router.get("/{id}", response_model=Colegio)
async def colegio(id: str):
    return search_colegio_id(id)

# GET colegio para mostrar todos sus alumnos
@router.get("/{id}/alumnos", response_model=list[Alumno])
async def colegio(id: str):
    try:
        colegio = colegio_schema(db_client.colegios.exm.find_one({"_id": ObjectId(id)}))
        Colegio(**colegio)
        return alumnos_schema(db_client.colegios.exm.id_colecio == id)
    except:
        return HTTPException(status_code=404, detail="Colegio no encontrado")

# POST añadir colegio
@router.post("/", response_model=Colegio, status_code=201)
async def add_colegio(colegio: Colegio):
    if type(search_colegio(colegio.nombre, colegio.distrito)) == Colegio:
        raise HTTPException(status_code=409, detail="Colegio ya existe")
    
    if (colegio.tipo == "publico") or (colegio.tipo == "concertado") or (colegio.tipo == "privado"):
        colegio_dict = colegio.model_dump()
        del colegio_dict["id"]
        id = db_client.colegios.exm.insert_one(colegio_dict).inserted_id
        colegio_dict["id"] = str(id)
        return Colegio(**colegio_dict)
    else:
        raise HTTPException(status_code=400, detail="Colegio no ha sido creado")
    
# DELETE colegio
@router.delete("/{id}", response_model=Colegio)
async def delete_colegio(id: str):
    found = db_client.colegios.exm.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        raise HTTPException(status_code=404, detail="Colegio no encontrado")
    return Colegio(**colegio_schema(found))

# Función auxiliar para buscar colegio por id
def search_colegio_id(id: str):
    try:
        colegio = colegio_schema(db_client.colegios.exm.find_one({"_id": ObjectId(id)}))
        return Colegio(**colegio)
    except:
        return HTTPException(status_code=404, detail="Colegio no encontrado")

# Función auxiliar para buscar colegio por nombre y distrito
def search_colegio(nombre: str, distrito: str):
    try:
        colegio = colegio_schema(db_client.colegios.exm.find_one({"nombre": nombre, "distrito": distrito}))
        return Colegio(**colegio)
    except:
        return HTTPException(status_code=404, detail="Colegio no encontrado")