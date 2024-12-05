from abc import ABC, abstractmethod

from yurenizer import NormalizerConfig


class NormalizeRepositoryInterface(ABC):
    @abstractmethod
    async def normalize_text(self, text: str, config: NormalizerConfig = NormalizerConfig()) -> str:
        pass


class NormalizeCsvRepositoryInterface(ABC):
    @abstractmethod
    async def normalize_csv(self, csv: str, config: NormalizerConfig = NormalizerConfig()) -> str:
        pass
