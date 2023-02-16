from fastapi import FastAPI

from app.core.config import settings

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
    import uvicorn

    uvicorn.run(
        app,
        host=settings.UVICORN_HOST,
        port=settings.UVICORN_PORT,
    )
