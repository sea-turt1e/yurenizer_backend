from fastapi import APIRouter

from app.api.endpoints import normalize

api_router = APIRouter()
api_router.include_router(normalize.router, tags=["normalize"])
