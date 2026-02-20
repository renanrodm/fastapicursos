from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession

from core.configs import settings

#Cria engine com as configurações definidas
engine: AsyncEngine = create_async_engine(settings.DB_URL)

#Cria a sessão do banco de dados. A função sessionmaker devolve de fato um classe.
Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)