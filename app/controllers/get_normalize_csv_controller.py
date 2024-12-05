import logging

from usecases.normalize_csv_usecase import NormalizeCsvUseCase
from yurenizer import NormalizerConfig

logger = logging.getLogger(__name__)


class GetNormalizeCsvController:
    def __init__(self, normalize_csv_usecase: NormalizeCsvUseCase):
        self.normalize_csv_usecase = normalize_csv_usecase

    async def execute(self, csv: str, config: NormalizerConfig) -> str:
        return await self.normalize_csv_usecase.execute(csv, config)
