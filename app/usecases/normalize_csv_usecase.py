import logging
from typing import List

from interfaces.repositories.normalize_repositry import NormalizeRepositoryInterface
from interfaces.usecases.normalize_csv_usecase import NormalizeCsvUseCaseInterface
from yurenizer import NormalizerConfig

logger = logging.getLogger(__name__)


class NormalizeCsvUseCase(NormalizeCsvUseCaseInterface):
    def __init__(self, repository: NormalizeRepositoryInterface):
        self.repository = repository

    async def execute(self, csv_rows: List[str], config: NormalizerConfig) -> List[str]:
        try:
            return [await self.repository.normalize_text(row, config) for row in csv_rows]
        except Exception as e:
            logger.error(f"error: {e}")
