from pydantic import BaseModel
from yurenizer import NormalizerConfig


class NormalizeTextRequest(BaseModel):
    config: NormalizerConfig = NormalizerConfig()


class NormalizeTextResponse(BaseModel):
    text: str


class NormalizeCsvRequest(BaseModel):
    config: NormalizerConfig = NormalizerConfig()
