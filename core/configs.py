#Configurações gerais acessiveis a qualquer parte do nosso projeto


from typing import ClassVar, List

from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:password@localhost:5432/faculdade'
    DBBaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()