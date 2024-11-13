from yurenizer import NormalizerConfig

from app.interfaces.repositories.normalize_text_repositry import NormalizeRepositoryInterface
from app.interfaces.usecases.normalize_text_usecase import NormalizeTextUseCaseInterface
from app.schemes.normalize import NormalizeTextResponse


class NormalizeTextUseCase(NormalizeTextUseCaseInterface):
    def __init__(self, repository: NormalizeRepositoryInterface):
        self.repository = repository

    async def execute(self, text: str, config: NormalizerConfig) -> NormalizeTextResponse:
        normalized_text = await self.repository.normalize_text(text, config)
        return NormalizeTextResponse(text=normalized_text, length=len(normalized_text))
