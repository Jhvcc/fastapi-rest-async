#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :connection.py
# @Author   :Lowell
# @Time     :2023/8/2 10:45
import motor.motor_asyncio
from beanie import init_beanie

from src.apps.auth.models import User
from src.core.config import settings


MONGO_DATABASE_URL = (f"mongodb://{settings.DB_USER}:{settings.DB_PASSWORD}@"
                      f"{settings.DB_HOST}:{settings.DB_PORT}")
client = motor.motor_asyncio.AsyncIOMotorClient(
    MONGO_DATABASE_URL, uuidRepresentation="standard"
)
database = client[settings.DB_DATABASE]


async def init_db():
    await init_beanie(
        database=database,
        document_models=[
            User
        ]
    )



