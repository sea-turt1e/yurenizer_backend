# 一時ファイルを削除する関数を定義
import logging
import os

logger = logging.getLogger(__name__)


def delete_file(path: str):
    try:
        os.remove(path)
        logger.info(f"一時ファイルを削除しました: {path}")
    except Exception as e:
        logger.error(f"一時ファイルの削除に失敗しました: {e}")
