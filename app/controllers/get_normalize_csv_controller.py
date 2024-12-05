import logging

from fastapi.responses import FileResponse
from schemes.normalize import NormalizeCsvRequest
from usecases.normalize_csv_usecase import NormalizeCsvUseCase
from yurenizer import NormalizerConfig

logger = logging.getLogger(__name__)


class GetNormalizeCsvController:
    def __init__(self, normalize_csv_usecase: NormalizeCsvUseCase):
        self.normalize_csv_usecase = normalize_csv_usecase

    async def execute(self, request: NormalizeCsvRequest, config: NormalizerConfig) -> FileResponse:
        return await self.normalize_csv_usecase.execute(request, config)
