from app.controllers.get_normalize_controller import GetNormalizeController
from app.usecases.normalize_text_usecase import NormalizeTextUsecase


def initilize():
    get_normalize_controller = GetNormalizeController(NormalizeTextUsecase())
    return get_normalize_controller


get_normalize_controller = initilize()
