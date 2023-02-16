from pydantic import BaseSettings


class Settings(BaseSettings):
    APPLICATION_NAME: str = "coreycothrum/fastapi_template"
    APPLICATION_VERSION: str = "0.0.0"
    APPLICATION_DESCRIPTION: str = "description coming soon..."

    API_PREFIX: str = "/api"
    API_V1_PATH: str = f"{API_PREFIX}/v1"
    API_V1_VERSION: str = "0.0.0"

    UVICORN_HOST: str = "0.0.0.0"
    UVICORN_PORT: int = 8000

    class Config:
        case_sensitive = True


settings = Settings()
