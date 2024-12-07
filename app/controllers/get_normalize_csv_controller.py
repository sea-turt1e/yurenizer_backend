import logging
from typing import List

from usecases.normalize_csv_usecase import NormalizeCsvUseCase
from yurenizer import NormalizerConfig

logger = logging.getLogger(__name__)


class GetNormalizeCsvController:
    def __init__(self, normalize_csv_usecase: NormalizeCsvUseCase):
        self.normalize_csv_usecase = normalize_csv_usecase

    async def execute(self, csv_content: str, config: NormalizerConfig) -> List[str]:
        csv_rows = csv_content.split("\n")
        if len(csv_rows) == 0:
            raise ValueError("csv file is empty")
        elif len(csv_rows) > 1000:
            raise ValueError("num of csv rows is too large")
        logger.info(f"csv_rows: {csv_rows}")
        return await self.normalize_csv_usecase.execute(csv_rows, config)
