from abc import ABC, abstractmethod

from schemes.normalize import NormalizeCsvRequest, NormalizeCsvResponse
from yurenizer import NormalizerConfig


class NormalizeCsvUseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, request: NormalizeCsvRequest, config: NormalizerConfig) -> NormalizeCsvResponse:
        pass
