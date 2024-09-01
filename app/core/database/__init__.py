# database/__init__.py

# lib
import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# module
from .models import *


# attribute
__all__ = []

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DB_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

ENGINE = create_async_engine(
    url=DB_URL
)

SESSION = async_sessionmaker(
    bind=ENGINE,
    class_=AsyncSession
)

# method
async def get_ss():
    try:
        ss = SESSION()
        yield ss
    except Exception as e:
        print("ERROR form get_ss : ", e)
        await ss.rollback()
    finally:
        await ss.close()

