from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(name=settings.APPLICATION_NAME, version=settings.APPLICATION_VERSION)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import os
    import uvicorn

    uvicorn.run(
        app,
        host=os.getenv("UVICORN_HOST", "0.0.0.0"),
        port=int(os.getenv("UVICORN_PORT", 8000)),
    )
