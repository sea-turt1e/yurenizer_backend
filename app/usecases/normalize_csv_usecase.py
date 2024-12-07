import logging

from fastapi.responses import FileResponse
from interfaces.repositories.normalize_repositry import NormalizeRepositoryInterface
from interfaces.usecases.normalize_csv_usecase import NormalizeCsvUseCaseInterface
from schemes.normalize import NormalizeCsvRequest
from yurenizer import NormalizerConfig

logger = logging.getLogger(__name__)


class NormalizeCsvUseCase(NormalizeCsvUseCaseInterface):
    def __init__(self, repository: NormalizeRepositoryInterface):
        self.repository = repository

    async def execute(self, request: NormalizeCsvRequest, config: NormalizerConfig) -> FileResponse:
        normalized_csv = await self.repository.normalize_csv(
            input_file_path=request.input_file_path, output_file_path=request.output_file_path, config=config
        )
        return FileResponse(content=normalized_csv)
