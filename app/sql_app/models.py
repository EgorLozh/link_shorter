import asyncio
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Column, Integer, MetaData, Text

from app.sql_app.engine import engine


class Base(DeclarativeBase): pass


class RedirectLink(Base):
    __tablename__ = "redirect_link"

    id = Column(Integer, primary_key=True)
    link = Column(Text, nullable=False, unique=True)
    redirect_endpoint = Column(Text, nullable=False, unique=True)



async_session = sessionmaker(
    bind=engine, 
    class_=AsyncSession,
    expire_on_commit=False
)

"""Первая версия"""
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)



"""Вторая версия"""
# import asyncio
# import asyncpg
# from app.config import *

# async def connect_postgres():
#     conn = await asyncpg.connect(user=DB_USER, password=DB_PASSWORD, database=DB_NAME, host=DB_HOST, port=DB_PORT)
#     try:
#         # Выполнение тестового запроса
#         result = await conn.fetch('SELECT version();')
#         print(result)
#     finally:
#         await conn.close()

# asyncio.run(connect_postgres())

