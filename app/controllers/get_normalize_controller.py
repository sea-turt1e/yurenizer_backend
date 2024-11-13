import logging

from yurenizer import NormalizerConfig

from app.usecases.normalize_text_usecase import NormalizeTextUseCase

logger = logging.getLogger(__name__)


class GetNormalizeController:
    def __init__(self, normalize_text_usecase: NormalizeTextUseCase):
        self.normalize_text_usecase = normalize_text_usecase

    async def execute(self, text: str, config: NormalizerConfig) -> str:
        return await self.normalize_text_usecase.execute(text, config)
