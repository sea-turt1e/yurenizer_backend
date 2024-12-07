from abc import ABC, abstractmethod

from yurenizer import NormalizerConfig


class NormalizeRepositoryInterface(ABC):
    @abstractmethod
    async def normalize_text(self, text: str, config: NormalizerConfig = NormalizerConfig()) -> str:
        pass

    @abstractmethod
    async def normalize_csv(
        self, input_file_path: str, output_file_path: str, config: NormalizerConfig = NormalizerConfig()
    ) -> str:
        pass
