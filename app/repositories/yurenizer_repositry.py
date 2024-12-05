from interfaces.repositories.normalize_repositry import NormalizeRepositoryInterface
from yurenizer import CsvSynonymNormalizer, NormalizerConfig, SynonymNormalizer


class YurenizerRepository(NormalizeRepositoryInterface):
    def __init__(self, synonym_file_path: str):
        self.normalizer = SynonymNormalizer(synonym_file_path)
        self.csv_normalizer = CsvSynonymNormalizer(synonym_file_path)

    async def normalize_text(self, text: str, config: NormalizerConfig = NormalizerConfig()) -> str:
        return self.normalizer.normalize(text, config)

    async def normalize_csv(
        self, input_file_path: str, output_file_path: str, config: NormalizerConfig = NormalizerConfig()
    ) -> None:
        return self.csv_normalizer.normalize_csv(input_file_path, output_file_path, config)
