from abc import ABC, abstractmethod

from yurenizer import NormalizerConfig


class NormalizeTextRepositoryInterface(ABC):
    @abstractmethod
    async def normalize_text(self, text: str, config: NormalizerConfig = NormalizerConfig()) -> str:
        pass
