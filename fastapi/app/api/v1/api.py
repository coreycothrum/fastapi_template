from fastapi import APIRouter

from app.api.v1.endpoints import server

api_router = APIRouter()
api_router.include_router(server.router, prefix="/server")
