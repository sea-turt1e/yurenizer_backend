from fastapi import Depends

from app.interfaces.usecases.normalize_text_usecase import NormalizeTextUseCaseInterface
from app.usecases.normalize_text_usecase import NormalizeTextUseCase


def get_normalize_text_usecase(normalize_text_usecase: NormalizeTextUseCaseInterface = Depends(NormalizeTextUseCase)):
    return normalize_text_usecase
