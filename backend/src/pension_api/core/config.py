from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Pension Calculator API"
    app_version: str = "1.0.0"

    debug: bool = False
    environment: str = "production"

    frontend_url: str = Field(
        default="http://localhost:5173",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
