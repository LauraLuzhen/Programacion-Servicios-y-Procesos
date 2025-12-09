# AUTOR(Id, DNI, Nombre, Apellidos)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/autores", tags=["autores"])

# Entidad Autor
class Autor(BaseModel):
    id: int
    dni: str
    nombre: str
    apellidos: str

# Listado de autores
autores_list = [
    Autor(id=1, dni="12345678A", nombre="Laura", apellidos="Rodríguez Morán"),
    Autor(id=2, dni="21436587B", nombre="Antonio", apellidos="Rodríguez García"),
    Autor(id=3, dni="87654321C", nombre="Elena", apellidos="Peña Morán"),
    Autor(id=4, dni="78563412D", nombre="Fernando", apellidos="García Peña"),
    Autor(id=5, dni="11223344E", nombre="David", apellidos="Villanueva Roldán")
]

# GET
# Todos los autores
@router.get("/")
def autores():
    return autores_list
# Método buscar por id
def search_id(id : int):
    autores = [autor for autor in autores_list if autor.id == id]
    if len(autores) != 0:
        return autores
    else:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
# Por id
@router.get("/{id}")
def autor_id(id : int):
    return search_id(id)
# Por query id
@router.get("")
def autor_queryid(id : int):
    return search_id(id)


# POST
@router.post("/", status_code=201, response_model=Autor)
def add_autor(autor : Autor):
    autor.id = next_id()
    autores_list.append(autor)
    return autor
# Método para conseguir el póximo id
def next_id():
    return (max(autores_list, key=id).id+1)


# PUT
@router.put("/{id}", response_model=Autor)
def modify_autor(id : int, autor : Autor):
    for index, saved in enumerate(autores_list):
        if saved.id == id:
            autor.id = id
            autores_list[index] = autor
            return autor
        else:
            raise HTTPException(status_code=404, detail="Autor no encontrado")
        
    
# DELETE
@router.delete("/{id}")
def delete_autor(id : int):
    for saved in autores_list:
        if saved.id == id:
            autores_list.remove(saved)
            return {}
        else:
            raise HTTPException(status_code=404, detail="Autor no encontrado")