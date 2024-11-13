from abc import ABC, abstractmethod

from yurenizer import NormalizerConfig

from app.schemes.normalize import NormalizeTextRequest, NormalizeTextResponse


class NormalizeTextUseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, request: NormalizeTextRequest, config: NormalizerConfig) -> NormalizeTextResponse:
        pass
