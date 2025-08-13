from dms.db.db import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

#dependency-injected functions
#provides an asynchronous SQLAlchemy database session to route functions
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
