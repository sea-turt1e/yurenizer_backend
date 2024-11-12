from pydantic import BaseModel


class NormalizeTextRequest(BaseModel):
    text: str


class NormalizeTextResponse(BaseModel):
    text: str
    length: int
