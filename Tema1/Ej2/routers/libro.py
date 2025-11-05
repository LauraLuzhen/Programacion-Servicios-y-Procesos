# LIBRO(Id, ISBN, Título, NumPaginas, IdAutor)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from routers.autor import autores_list

router = APIRouter(prefix="/libros", tags=["libros"])

# Entidad Libro
class Libro(BaseModel):
    id : int
    isbn: str
    titulo: str
    num_paginas: int
    id_autor: int

# Listado de libros
libros_list = [
    Libro(id=1, isbn="ISBN12345678", titulo="Progrmación de Servicios y Procesos", num_paginas=153, id_autor=2),
    Libro(id=2, isbn="ISBN87654321", titulo="Aplicaciones móviles", num_paginas=260, id_autor=1),
    Libro(id=3, isbn="ISBN21436587", titulo="Acceso a Datos", num_paginas=110, id_autor=3),
    Libro(id=4, isbn="ISBN78563412", titulo="IPE", num_paginas=144, id_autor=4),
    Libro(id=5, isbn="ISBN11223344", titulo="Base de datos", num_paginas=202, id_autor=1),
]

# GET
# Todos los libros
@router.get("/")
def libros():
    return libros_list
# Método que búsca por id
def search_id(id : int):
    libros = [libro for libro in libros_list if libro.id == id]
    if len(libros) != 0:
        return libros
    else:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
# Por id
@router.get("/{id}")
def director_id(id : int):
    return search_id(id)
# Por id query
@router.get("")
def director_queryid(id : int):
    return search_id(id)


# POST
@router.post("/", status_code=201, response_model=Libro)
def add_libro(libro: Libro):
    libro.id = next_id()
    autores_id = [autor.id for autor in autores_list]
    if libro.id_autor not in autores_id:
        raise HTTPException(status_code=404, detail="El id del autor no existe")
    else:
        libros_list.append(libro)
        return libro
# Método para conseguir el próximo id
def next_id():
    return (max(libros_list, key=id).id+1)


# PUT
@router.put("/{id}", response_model=Libro)
def modify_libro(id : int, libro : Libro):
    for index, saved in enumerate(libros_list):
        if saved.id == id:
            libro.id = id
            autores_id = [autor.id for autor in autores_list]
            if libro.id_autor not in autores_id:
                raise HTTPException(status_code=404, detail="El id del autor no existe")
            else:
                libros_list[index] = libro
                return libro
        else:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        

# DELETE
@router.delete("/{id}")
def delete_libro(id : int):
    for saved in libros_list:
        if saved.id == id:
            libros_list.remove(saved)
            return {}
        else:
            raise HTTPException(status_code=404, detail="Libro no encontrado")