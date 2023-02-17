import ipaddress
import logging
from typing import Any, Optional

from pydantic import BaseSettings, PositiveInt, PostgresDsn, validator

from app.core.version import PydanticVersion


class Settings(BaseSettings):
    APPLICATION_NAME: str = "coreycothrum/fastapi_template"
    APPLICATION_DESCRIPTION: str = "description coming soon..."
    APPLICATION_VERSION: PydanticVersion = "0.0.0"

    API_PREFIX: str = "/api"

    API_V1_VERSION: PydanticVersion = "1.0.0"
    API_V1_PATH: str = f"{API_PREFIX}/v1"

    LOGGING_FORMAT: str = (
        "%(levelname)s@%(asctime)s@%(module)s.%(funcName)s: %(message)s"
    )
    LOGGING_LEVEL: PositiveInt = logging.INFO

    POSTGRES_HOST: str
    POSTGRES_PORT: PositiveInt = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URI: Optional[PostgresDsn] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=f"{values.get('POSTGRES_HOST')}:{values.get('POSTGRES_PORT')}",
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    UVICORN_HOST: ipaddress.IPv4Address = "0.0.0.0"
    UVICORN_PORT: PositiveInt = 8000

    class Config:
        case_sensitive = True


settings = Settings()

logging.basicConfig(format=settings.LOGGING_FORMAT, level=settings.LOGGING_LEVEL)
logger = logging.getLogger(settings.APPLICATION_NAME)
