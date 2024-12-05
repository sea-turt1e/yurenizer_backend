from abc import ABC, abstractmethod

from fastapi.responses import FileResponse
from schemes.normalize import NormalizeCsvRequest
from yurenizer import NormalizerConfig


class NormalizeCsvUseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, request: NormalizeCsvRequest, config: NormalizerConfig) -> FileResponse:
        pass
