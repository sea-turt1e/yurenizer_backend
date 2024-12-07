from abc import ABC, abstractmethod

from yurenizer import NormalizerConfig


class NormalizeCsvUseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, csv_rows: list[str], config: NormalizerConfig) -> list:
        pass
