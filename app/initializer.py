import logging
import logging.config

from controllers.get_normalize_controller import GetNormalizeController
from repositories.yurenizer_repositry import YurenizerRepository
from usecases.normalize_text_usecase import NormalizeTextUseCase

logging.config.fileConfig("logging_debug.conf")
logger = logging.getLogger(__name__)


def initilize():
    # シノニムファイルのパスを指定
    synonym_file_path = "data/synonyms.txt"

    # YurenizerRepositoryをインスタンス化
    repository = YurenizerRepository(synonym_file_path)

    normalize_text_usecase = NormalizeTextUseCase(repository)
    get_normalize_controller = GetNormalizeController(normalize_text_usecase)
    return get_normalize_controller


get_normalize_controller = initilize()
