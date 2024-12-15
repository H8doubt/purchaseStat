from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker,
                                    AsyncAttrs)
from sqlalchemy.orm import sessionmaker
import asyncio

DATABASE_URL = "postgresql+asyncpg://pguser:pgpwd4purchstat@localhost:6432/purchasestatdb"

Base = declarative_base()

#engine = create_engine(DATABASE_URL, echo=True)
engine = create_async_engine(url=DATABASE_URL)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
