from app.controllers.get_normalize_controller import GetNormalizeController
from app.repositories.yurenizer_repositry import YurenizerRepository
from app.usecases.normalize_text_usecase import NormalizeTextUseCase


def initilize():
    # シノニムファイルのパスを指定
    synonym_file_path = "app/data/synonyms.txt"

    # YurenizerRepositoryをインスタンス化
    repository = YurenizerRepository(synonym_file_path)

    normalize_text_usecase = NormalizeTextUseCase(repository)
    get_normalize_controller = GetNormalizeController(normalize_text_usecase)
    return get_normalize_controller


get_normalize_controller = initilize()
