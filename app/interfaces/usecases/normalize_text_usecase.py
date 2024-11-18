from abc import ABC, abstractmethod

from schemes.normalize import NormalizeTextRequest, NormalizeTextResponse
from yurenizer import NormalizerConfig


class NormalizeTextUseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, request: NormalizeTextRequest, config: NormalizerConfig) -> NormalizeTextResponse:
        pass
