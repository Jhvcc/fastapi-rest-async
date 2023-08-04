#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :dependence.py
# @Author   :Lowell
# @Time     :2023/8/2 11:14
from beanie import PydanticObjectId
from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend
from fastapi_users_db_beanie import BeanieUserDatabase

from src.apps.auth.manager import UserManager, SECRET
from src.apps.auth.models import User, OAuthAccount


async def get_user_db():
    yield BeanieUserDatabase(User, OAuthAccount)


async def get_user_manager(
    user_db: BeanieUserDatabase = Depends(get_user_db)
):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)

