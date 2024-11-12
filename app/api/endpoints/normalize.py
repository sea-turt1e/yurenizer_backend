from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.api.deps import get_normalize_text_usecase
from app.initializer import get_normalize_controller
from app.interfaces.usecases.normalize_text_usecase import NormalizeTextUseCaseInterface
from app.schemes.normalize import NormalizeTextRequest, NormalizeTextResponse  # NormalizeTextResponseをインポート

router = APIRouter()


@router.get("/normalize_text", response_model=NormalizeTextResponse)
async def normalize(
    text: str,
    controller=Depends(lambda: get_normalize_controller),
):
    result = await controller.execute(text)
    return NormalizeTextResponse(text=result.text, length=result.length)
