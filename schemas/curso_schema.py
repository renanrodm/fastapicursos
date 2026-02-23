"""
    Para cada model teremos um schema.
"""


from typing import Optional
from pydantic import BaseModel as SCBaseModel



class CursoSchema(SCBaseModel):
    id: Optional[int] = None #Opcional porque é criado pelo proprio banco de dados.
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True
