from core.configs import settings

from sqlalchemy import Column, Integer, String, Float

class CursoModel(settings.DB_BASE_MODEL):
    __tablename__ = 'cursos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo:str = Column(String(100), nullable=False)
    aulas: int = Column(Integer, nullable=False)
    horas: float = Column(Float, nullable=False)   