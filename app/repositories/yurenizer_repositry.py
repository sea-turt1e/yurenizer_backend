from interfaces.repositories.normalize_text_repositry import NormalizeTextRepositoryInterface
from yurenizer import NormalizerConfig, SynonymNormalizer


class YurenizerRepository(NormalizeTextRepositoryInterface):
    def __init__(self, synonym_file_path: str):
        self.normalizer = SynonymNormalizer(synonym_file_path)

    async def normalize_text(self, text: str, config: NormalizerConfig = NormalizerConfig()) -> str:
        return self.normalizer.normalize(text, config)
