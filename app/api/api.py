from api.endpoints import healthcheck, normalize_csv, normalize_text
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(healthcheck.router)
api_router.include_router(normalize_text.router, tags=["normalize"])
api_router.include_router(normalize_csv.router, tags=["normalize"])
