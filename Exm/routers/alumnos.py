from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db.client import db_client
from db.schemas.alumnos import alumno_schema, alumnos_schema  
from db.models.alumnos import Alumno
from db.schemas.colegios import colegio_schema  
from db.models.colegios import Colegio  

router = APIRouter(prefix="/alumnos_db", tags=["alumnos_db"])

# GET todos los alumnos
@router.get("/", response_model=list[Alumno])
async def alumnos():
    return alumnos_schema(db_client.alumnos.exm.find())

# GET alumno por query id
@router.get("", response_model=Alumno)
async def alumno(id: str):
    return search_alumno_id(id)

# POST añadir alumno
@router.post("/", response_model=Alumno, status_code=201)
async def add_alumno(alumno: Alumno):
    if type(search_colegio(alumno.id_colegio)) == Alumno:
        raise HTTPException(status_code=409, detail="Colegio no existe")
    
    alumno_dict = alumno.model_dump()
    del alumno_dict["id"]
    id = db_client.alumnos.exm.insert_one(alumno_dict).inserted_id
    alumno_dict["id"] = str(id)
    return Alumno(**alumno_dict)

# PUT modificar alumno
@router.put("/{id}", response_model=Alumno)
async def modify_alumno(id: str, new_alumno: Alumno):
    alumno_dict = new_alumno.model_dump()
    del alumno_dict["id"]
    try:
        if search_colegio(new_alumno.id_colegio) == Alumno:
            raise HTTPException(status_code=409, detail="Colegio no existe")
        db_client.alumnos.exm.find_one_and_replace({"_id": ObjectId(id)}, alumno_dict)
        return search_alumno_id(id)
    except:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

# DELETE alumno
@router.delete("/{id}", response_model=Alumno)
async def delete_alumno(id: str):
    found = db_client.alumnos.exm.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return Alumno(**alumno_schema(found))

# Función auxiliar para buscar alumno por id
def search_alumno_id(id: str):
    try:
        alumno = alumno_schema(db_client.alumnos.exm.find_one({"_id": ObjectId(id)}))
        return Alumno(**alumno)
    except:
        return HTTPException(status_code=404, detail="Alumno no encontrado")
    
# Función auxiliar para buscar colegio por su id
def search_colegio(id: int):
    try:
        colegio = colegio_schema(db_client.colegios.exm.find_one({"id": id}))
        return Colegio(**colegio)
    except:
        return HTTPException(status_code=404, detail="Colegio no encontrado")
