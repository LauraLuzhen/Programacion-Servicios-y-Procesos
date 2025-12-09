from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Entidad Asignatura
# (Id, Título, NumHoras, IdProfesor)
class Asignatura(BaseModel):
    id: int
    titulo: str
    num_horas: int
    id_profesor: int

asignaturas_list = [
    Asignatura(id=1, titulo="Matemáticas", num_horas=120, id_profesor=2),
    Asignatura(id=2, titulo="Historia", num_horas=100, id_profesor=2),
    Asignatura(id=3, titulo="Lengua", num_horas=110, id_profesor=3)
]

