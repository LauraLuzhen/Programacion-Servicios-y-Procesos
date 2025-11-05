from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Entidad Profesor
# (Id, DNI, Nombre, Apellidos, Teléfono, Dirección, CuentaBancaria)
class Profesor(BaseModel):
    id: int
    dni: str
    nombre: str
    apellidos: str
    telefono: int
    direccion: str
    cuenta_bancaria: str

profesores_list = [
    Profesor(id=1, dni="12345678A", nombre="Juan", apellidos="Pérez", telefono=600123456, direccion="Calle Falsa 123", cuenta_bancaria="ES7620770024003102575766"),
    Profesor(id=2, dni="87654321B", nombre="María", apellidos="Gómez", telefono=600654321, direccion="Avenida Siempre Viva 742", cuenta_bancaria="ES9121000418450200051332"),
    Profesor(id=3, dni="11223344C", nombre="Luis", apellidos="Martínez", telefono=600112233, direccion="Plaza Mayor 1", cuenta_bancaria="ES5600491500051234567891")
]

# Todos los profesores
@router.get("/")
def get_profesores():
    return profesores_list

# Función para buscar profesor por id
def search_profesor(id: int):
    profesores = [profesor for profesor in profesores_list if profesor.id == id]

    if len(profesores) != 0:
        return profesores
    raise HTTPException(status_code=404, detail="Profesor no encontrado")

# Por el id
@router.get("/{id}")
def get_porid(id: int):
    return search_profesor(id)

# Por query id
@router.get("/by_id/")
def get_porquery(id: int):
    return search_profesor(id)

# POST
# Conseguimos el próximo id
def next_id():
    return (max(profesores_list, key=id).id + 1)

# Realizamos el post
@router.post("/", status_code=201, response_model=Profesor)
def create_profesor(profesor: Profesor):
    profesor.id = next_id()
    profesores_list.append(profesor)
    return profesor

# PUT
@router.put("/{id}", response_model=Profesor)
def update_profesor(id: int, profesor: Profesor):
    for index, saved_profesor in enumerate(profesores_list):
        if saved_profesor.id == id:
            profesor.id = id
            profesores_list[index] = profesor
            return profesor
    raise HTTPException(status_code=404, detail="Profesor no encontrado")

# DELETE
@router.delete("/{id}")
def delete_profesor(id: int):
    for saved_profesor in profesores_list:
        if saved_profesor.id == id:
            profesores_list.remove(saved_profesor)
            return {"message": "Profesor eliminado"}
    raise HTTPException(status_code=404, detail="Profesor no encontrado")