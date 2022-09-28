from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id:Optional[int] = None
    titulo: str
    aulas: int
    horas:int




cursos = [
    Curso(id=1,titulo='Curso 1 Codevibes', aulas= 10, horas = 10),
    Curso(id=2,titulo='Curso 2 Codevibes', aulas= 20, horas = 20),
    Curso(id=3,titulo='Curso 3 Codevibes', aulas= 30, horas = 30),
    Curso(id=4,titulo='Curso 4 Codevibes', aulas= 40, horas = 40),
    Curso(id=5,titulo='Curso 5 Codevibes', aulas= 50, horas = 50),
    Curso(id=6,titulo='Curso 6 Codevibes', aulas= 60, horas = 60),
    Curso(id=7,titulo='Curso 7 Codevibes', aulas= 70, horas = 70),
    Curso(id=8,titulo='Curso 8 Codevibes', aulas= 80, horas = 80),  
]