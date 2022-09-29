from pydantic import BaseModel
from typing import Optional

class Curso(BaseModel):
    id:Optional[int] = None
    titulo: str
    aulas: int


cursos = [
    Curso(id=1, titulo="Curso 1",aulas=10),
    Curso(id=2, titulo="Curso 2",aulas=20),
    Curso(id=3, titulo="Curso 3",aulas=20),
    Curso(id=4, titulo="Curso 4",aulas=30)
]