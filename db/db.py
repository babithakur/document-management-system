from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dms.config.config import DATABASE_URL

#async engine and session setup using SQLAlchemy and asyncpg
#creates an asynchronous SQLAlchemy engine for connecting PostgreSQL database using an async driver like asyncpg
#this engine manages connections, connection pooling, and DB communication
engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)
