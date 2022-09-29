from http.client import HTTPException
from fastapi import Path
from fastapi import APIRouter, status

from typing import List

from model.model import Curso, cursos

router = APIRouter()


@router.get('/api/v1/cursos', status_code=status.HTTP_200_OK, response_description="Retorna cursos",response_model=List[Curso])
async def get_cursos():
  try:
    return cursos
  except:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nada encontrado")

@router.get('/api/v1/cursos/{curso_id}', status_code=status.HTTP_200_OK, response_model=Curso, summary="Get By ID")
async def get_cursos(curso_id: int = Path(default=None, title="get_cursos",description="Filtro para get cursos", gt=0,lt=10)):
  return cursos[curso_id - 1]


