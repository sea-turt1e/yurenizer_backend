import logging

from fastapi import APIRouter, Depends
from yurenizer import NormalizerConfig

from app.controllers.get_normalize_controller import GetNormalizeController
from app.initializer import get_normalize_controller
from app.schemes.normalize import NormalizeTextRequest, NormalizeTextResponse

router = APIRouter()


@router.post("/normalize_text", response_model=NormalizeTextResponse)
async def normalize_text(
    text: str,
    request: NormalizeTextRequest,
    controller: GetNormalizeController = Depends(lambda: get_normalize_controller),
):
    config = request.config
    normalizer_config = NormalizerConfig(
        unify_level=config.unify_level,
        taigen=config.taigen,
        yougen=config.yougen,
        expansion=config.expansion,
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
    result = await controller.execute(text, normalizer_config)
    return NormalizeTextResponse(text=result.text)
