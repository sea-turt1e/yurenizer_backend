from pydantic import BaseModel


class Settings(BaseModel):
    LIMIT_TEXT_LENGTH: int = 300


settings = Settings()
