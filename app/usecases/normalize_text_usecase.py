from yurenizer import SynonymNormalizer


class NormalizeTextUsecase:
    def __init__(self) -> None:
        self.synonym_nomalizer = SynonymNormalizer("app/data/synonyms.txt")

    def execute(self, text) -> str:
        return self.synonym_nomalizer.normalize(text)
