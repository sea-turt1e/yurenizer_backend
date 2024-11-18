from api.endpoints import healthcheck, normalize
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(normalize.router, tags=["normalize"])
api_router.include_router(healthcheck.router, tags=["healthcheck"])
