from pydantic import BaseModel


class Settings(BaseModel):
    LIMIT_TEXT_LENGTH: int = 1000


settings = Settings()
