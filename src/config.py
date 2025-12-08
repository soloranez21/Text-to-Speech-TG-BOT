"""
Application configuration.

Loads settings from environment variables.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_bot_token: str
    google_api_key: str
    max_text_length: int = 20000

    class Config:
        env_file = ".env"


settings = Settings()
