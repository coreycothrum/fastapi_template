from pydantic import BaseSettings


class Settings(BaseSettings):
    APPLICATION_NAME: str = "coreycothrum/fastapi_template"
    APPLICATION_VERSION: str = "0.0.0"

    class Config:
        case_sensitive = True


settings = Settings()
