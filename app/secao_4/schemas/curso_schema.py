from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CursoSchema(SCBaseModel):
    id:Optional[int]
    titulo:str
    aulas:int
    horas:float

    class config:
        orm_mode = True

