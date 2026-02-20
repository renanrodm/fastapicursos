from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session


async def get_session() -> Generator:
    """
        Dependência para executar a sessão do banco de dados
    """
    session: AsyncSession = Session()

    try:
        #Apenas devolve a sessão para uso e para aqui.
        yield session
    finally:
        await session.close()
