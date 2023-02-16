from fastapi import APIRouter, status

from app import schemas

router = APIRouter(tags=["server"])


@router.get(
    "/info",
    response_model=schemas.server.ServerDetail,
    status_code=status.HTTP_200_OK,
    description="Return information about the connected server",
)
async def get_server_information():
    return schemas.server.ServerDetail()
