from interfaces.repositories.normalize_text_repositry import NormalizeTextRepositoryInterface
from interfaces.usecases.normalize_text_usecase import NormalizeTextUseCaseInterface
from schemes.normalize import NormalizeTextResponse
from yurenizer import NormalizerConfig


class NormalizeTextUseCase(NormalizeTextUseCaseInterface):
    def __init__(self, repository: NormalizeTextRepositoryInterface):
        self.repository = repository

    async def execute(self, text: str, config: NormalizerConfig) -> NormalizeTextResponse:
        normalized_text = await self.repository.normalize_text(text, config)
        return NormalizeTextResponse(text=normalized_text, length=len(normalized_text))
