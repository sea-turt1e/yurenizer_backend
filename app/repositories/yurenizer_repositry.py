from interfaces.repositories.normalize_text_repositry import NormalizeRepositoryInterface
from yurenizer import NormalizerConfig, SynonymNormalizer


class YurenizerRepository(NormalizeRepositoryInterface):
    def __init__(self, synonym_file_path: str):
        self.normalizer = SynonymNormalizer(synonym_file_path)

    async def normalize_text(self, text: str, config: NormalizerConfig = NormalizerConfig()) -> str:
        return self.normalizer.normalize(text, config)
