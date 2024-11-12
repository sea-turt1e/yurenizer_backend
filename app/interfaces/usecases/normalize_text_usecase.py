from abc import ABC, abstractmethod

from app.schemes.normalize import NormalizeTextRequest, NormalizeTextResponse


class NormalizeTextUseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, request: NormalizeTextRequest) -> NormalizeTextResponse:
        pass
