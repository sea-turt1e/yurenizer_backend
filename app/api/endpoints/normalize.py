from fastapi import APIRouter, Depends

from app.initializer import get_normalize_controller

router = APIRouter()


@router.get("/normalize")
def normalize(text: str):
    try:
        normalized_text = get_normalize_controller.execute(text)
        return {"status": "ok", "message": normalized_text}
    except Exception as e:
        return {"status": "error", "message": str(e)}
