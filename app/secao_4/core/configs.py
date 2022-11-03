from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from env.secrets import secrets

class Settings(BaseSettings):
    '''
    Configurações usadas na aplicação
    '''
    API_V1_STR: str = 'api/v1'
    DB_URL: str = f'mysql+aiomysql://{secrets.get("user")}:{secrets.get("password")}@localhost/faculdade'
    # DB_URL: str = "sqlite+aiosqlite:///./test.db"
    DB_BASE_MODEL = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()