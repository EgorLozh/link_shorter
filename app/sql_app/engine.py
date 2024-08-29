from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from functools import lru_cache
from app.config import DB_URL


engine = create_async_engine(DB_URL)
session_maker = async_sessionmaker( engine, class_=AsyncSession, expire_on_commit=False)

@lru_cache(1)
def get_session():
    return session_maker()