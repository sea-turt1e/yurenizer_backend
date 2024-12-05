from abc import ABC, abstractmethod

from yurenizer import NormalizerConfig


class NormalizeCsvRepositoryInterface(ABC):
    @abstractmethod
    async def normalize_csv(self, csv: str, config: NormalizerConfig = NormalizerConfig()) -> str:
        pass
