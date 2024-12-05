import logging

from fastapi.responses import FileResponse
from interfaces.repositories.normalize_repositry import NormalizeCsvRepositoryInterface
from interfaces.usecases.normalize_csv_usecase import NormalizeCsvUseCaseInterface
from schemes.normalize import NormalizeCsvRequest
from yurenizer import NormalizerConfig

logger = logging.getLogger(__name__)


class NormalizeCsvUseCase(NormalizeCsvUseCaseInterface):
    def __init__(self, repository: NormalizeCsvRepositoryInterface):
        self.repository = repository

    async def execute(self, request: NormalizeCsvRequest, config: NormalizerConfig) -> FileResponse:
        normalized_csv = await self.repository.normalize_csv(request.csv, config)
        return FileResponse(content=normalized_csv)
