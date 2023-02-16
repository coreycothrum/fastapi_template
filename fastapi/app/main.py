from fastapi import FastAPI

from app.core.config import settings
from app.core.config import logger

app = FastAPI(name=settings.APPLICATION_NAME, version=settings.APPLICATION_VERSION)

################################################################################
# API_V1
################################################################################
api_v1 = FastAPI(
    name=settings.APPLICATION_NAME,
    version=settings.API_V1_VERSION,
    description=settings.APPLICATION_DESCRIPTION,
    openapi_url=f"{settings.API_V1_PATH}/openapi.json",
)


@api_v1.get("/")
async def root():
    return {"message": "Hello World"}


app.mount(f"{settings.API_V1_PATH}", api_v1)

################################################################################
################################################################################
################################################################################
if __name__ == "__main__":
    logger.info(f"starting {settings.APPLICATION_NAME}")

    import uvicorn

    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = settings.LOGGING_FORMAT
    log_config["formatters"]["default"]["fmt"] = settings.LOGGING_FORMAT

    uvicorn.run(
        app,
        host=settings.UVICORN_HOST,
        port=settings.UVICORN_PORT,
        log_config=log_config,
    )
