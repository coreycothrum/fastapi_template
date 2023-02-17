from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

async_database_engine = create_async_engine(
    settings.DATABASE_URI, echo=False, future=True, pool_pre_ping=True
)
async_database_session = sessionmaker(
    async_database_engine, class_=AsyncSession, expire_on_commit=False
)


async def get_database() -> AsyncSession:
    async with async_database_session() as database:
        yield database


################################################################################
################################################################################
################################################################################
async def verify_database_connection() -> bool:
    async for database in get_database():
        await database.execute(text("SELECT 1"))


def main() -> None:
    import asyncio
    from app.core.config import logger

    logger.info("initializing database session")
    logger.info("verifying connection to database")

    asyncio.run(verify_database_connection())


if __name__ == "__main__":
    main()
