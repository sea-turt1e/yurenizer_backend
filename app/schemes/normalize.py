from pydantic import BaseModel


class NomalizedResponse(BaseModel):
    text: str
    length: int
    normalized_text: str
