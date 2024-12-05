import json
import logging

import aiofiles
from controllers.get_normalize_csv_controller import GetNormalizeCsvController
from fastapi import APIRouter, Depends, File, Form, UploadFile
from fastapi.responses import FileResponse
from initializer import get_normalize_csv_controller
from schemes.normalize import NormalizeCsvRequest
from yurenizer import NormalizerConfig

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/normalize_csv")
async def normalize_csv(
    file: UploadFile = File(...),
    request: NormalizeCsvRequest = Depends(),
    controller: GetNormalizeCsvController = Depends(lambda: get_normalize_csv_controller),
) -> FileResponse:
    logger.info("Get request to /normalize_csv")
    # return FileResponse(path=file, filename="test.csv", media_type="text/csv")
    contens = await file.read()
    csv_content = contens.decode("utf-8")
    if len(csv_content) == 0:
        raise ValueError("csv file is empty")
    elif len(csv_content) > 1000:
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
        normalized_csv_content = await controller.execute(csv_content, normalizer_config)
        logger.info(f"normalized_csv_content: {normalized_csv_content}")
    except Exception as e:
        logger.error(f"error: {e}")
        raise e
    else:
        # 一時ファイルに書き込み
        async with aiofiles.tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv") as tmp:
            temp_file_path = tmp.name
            logger.info(f"temp_file_path: {temp_file_path}")
            await tmp.write(normalized_csv_content)

            # ファイルをレスポンスとして返す
            return FileResponse(path=temp_file_path, filename="normalized.csv", media_type="text/csv")
