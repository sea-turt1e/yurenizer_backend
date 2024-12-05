import logging

from controllers.get_normalize_text_controller import GetNormalizeTextController
from fastapi import APIRouter, Depends
from initializer import get_normalize_text_controller
from schemes.normalize import NormalizeTextRequest, NormalizeTextResponse
from yurenizer import NormalizerConfig

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/normalize_text", response_model=NormalizeTextResponse)
async def normalize_text(
    text: str,
    request: NormalizeTextRequest,
    controller: GetNormalizeTextController = Depends(lambda: get_normalize_text_controller),
):
    logger.info("Get request to /normalize_text")
    logger.info(f"text: {text}")
    if len(text) > 1000:
        raise ValueError("The text is too long. Please input text less than 1000 characters.")
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
        result = await controller.execute(text, normalizer_config)
        logger.info(f"result: {result}")
    except Exception as e:
        logger.error(f"error: {e}")
        raise e
    return NormalizeTextResponse(text=result.text)
