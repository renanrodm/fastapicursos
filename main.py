from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - FastAPI SQL Alchemy')
app.include_router(api_router, prefix=settings.API_V1_STR)
# settings.API_V1_STR vai trazer /api/v1/endpoints

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)