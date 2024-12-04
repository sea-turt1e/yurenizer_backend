import logging

from controllers.get_normalize_controller import GetNormalizeController
from fastapi import APIRouter, Depends
from initializer import get_normalize_controller
from schemes.normalize import NormalizeCsvRequest, NormalizeCsvResponse
from yurenizer import NormalizerConfig

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/normalize_csv", response_model=NormalizeCsvResponse)
async def normalize_csv(
    request,
) -> NormalizeCsvResponse:
    logger.info("Get request to /normalize_csv")
    with open("test.csv", "r") as f:
        if len(f.read()) == 0:
            raise ValueError("csv file is empty")
        elif len(f.read()) > 1000:
            raise ValueError("csv file is too large")
    config = request.config
    normalizer_config = NormalizerConfig(
        taigen=config.taigen,
        yougen=config.yougen,
        expansion=config.expansion,
        unify_level=config.unify_level,
        other_language=config.other_language,
        alias=config.alias,
        old_name=config.old_name,
        misuse=config.misuse,
        alphabetic_abbreviation=config.alphabetic_abbreviation,
        non_alphabetic_abbreviation=config.non_alphabetic_abbreviation,
        alphabet=config.alphabet,
        orthographic_variation=config.orthographic_variation,
        misspelling=config.misspelling,
        custom_synonym=config.custom_synonym,
    )
    logger.info(f"normalizer_config: {normalizer_config}")
    try:
        result = await controller.execute(csv, normalizer_config)
        logger.info(f"result: {result}")
    except Exception as e:
        logger.error(f"error: {e}")
        raise e
    return NormalizeCsvResponse(result=result)
