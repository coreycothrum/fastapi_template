import ipaddress
import logging

from pydantic import BaseSettings, PositiveInt

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

    UVICORN_HOST: ipaddress.IPv4Address = "0.0.0.0"
    UVICORN_PORT: PositiveInt = 8000

    class Config:
        case_sensitive = True


settings = Settings()

logging.basicConfig(format=settings.LOGGING_FORMAT, level=settings.LOGGING_LEVEL)
logger = logging.getLogger(settings.APPLICATION_NAME)
