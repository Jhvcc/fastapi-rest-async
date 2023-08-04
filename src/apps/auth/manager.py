#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :manage.py
# @Author   :Lowell
# @Time     :2023/8/2 11:20
from typing import Optional

from beanie import PydanticObjectId
from fastapi_users import BaseUserManager
from fastapi_users_db_beanie import ObjectIDIDMixin
from starlette.requests import Request

from src.apps.auth.models import User

SECRET = "SECRET"


class UserManager(ObjectIDIDMixin, BaseUserManager[User, PydanticObjectId]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self, user: User, request: Optional[Request] = None
    ) -> None:
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ) -> None:
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ) -> None:
        print(f"Verification requested for user {user.id}. Verification token: {token}")

