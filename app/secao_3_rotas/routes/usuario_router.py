from turtle import title
from fastapi import APIRouter

router = APIRouter()


@router.get('/api/v1/usuarios', description="Rota para busca de lista de usuários", summary="Lista de usuários", response_description='Usuários')
async def get_usuarios():
  return {'info': "todos os usuarios"}