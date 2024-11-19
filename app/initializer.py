import logging
import logging.config
import os

from controllers.get_normalize_controller import GetNormalizeController
from repositories.yurenizer_repositry import YurenizerRepository
from usecases.normalize_text_usecase import NormalizeTextUseCase

log_config = "logging_lambda.conf" if os.getenv("AWS_LAMBDA_FUNCTION_NAME") else "logging_debug.conf"
logging.config.fileConfig(log_config)
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
