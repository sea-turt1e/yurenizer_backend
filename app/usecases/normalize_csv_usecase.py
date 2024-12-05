from interfaces.repositories.normalize_csv_repositry import NormalizeCsvRepositoryInterface
from interfaces.usecases.normalize_csv_usecase import NormalizeCsvUseCaseInterface
from schemes.normalize import NormalizeCsvResponse
from yurenizer import NormalizerConfig


class NormalizeCsvUseCase(NormalizeCsvUseCaseInterface):
    def __init__(self, repository: NormalizeCsvRepositoryInterface):
        self.repository = repository

    async def execute(self, csv: str, config: NormalizerConfig) -> NormalizeCsvResponse:
        normalized_csv = await self.repository.normalize_csv(csv, config)
        return NormalizeCsvResponse(csv=normalized_csv, length=len(normalized_csv))
