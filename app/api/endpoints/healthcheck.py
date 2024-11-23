import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/healthcheck")
def healthcheck():
    logger.info("get request to /healthcheck")
    return {"status": "ok"}
