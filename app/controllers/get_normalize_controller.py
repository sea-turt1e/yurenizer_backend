import logging

from app.usecases.normalize_text_usecase import NormalizeTextUsecase

logger = logging.getLogger(__name__)


class GetNormalizeController:
    def __init__(
        self,
        normalize_text_usecase: NormalizeTextUsecase,
    ) -> None:
        self.normalize_text_usecase = normalize_text_usecase

    def execute(self, text: str):
        try:
            normalized_text = self.normalize_text_usecase.execute(text)
            return {"status": "ok", "message": normalized_text}
        except Exception as e:
            logger.error(e)
            return {"status": "error", "message": str(e)}
