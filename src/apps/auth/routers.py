#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :router.py
# @Author   :Lowell
# @Time     :2023/8/2 11:10
from fastapi import APIRouter, Depends

from src.apps.auth.dependence import current_active_user, fastapi_users, auth_backend
from src.apps.auth.manager import SECRET
from src.apps.auth.models import User
from src.apps.auth.oauth2 import google_oauth2_client, microsoft_oauth2_client, github_oauth2_client
from src.apps.auth.schemas import BaseUser, UserUpdate, UserCreate

api_router = APIRouter()


api_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)
api_router.include_router(
    fastapi_users.get_register_router(BaseUser, UserCreate),
    prefix="/auth",
    tags=["auth"]
)
api_router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"]
)
api_router.include_router(
    fastapi_users.get_verify_router(BaseUser),
    prefix="/auth",
    tags=["auth"]
)
api_router.include_router(
    fastapi_users.get_users_router(BaseUser, UserUpdate),
    prefix="/user",
    tags=["user"]
)
api_router.include_router(
    fastapi_users.get_oauth_router(google_oauth2_client, auth_backend, SECRET),
    prefix="/auth/google",
    tags=["auth"],
)
api_router.include_router(
    fastapi_users.get_oauth_router(github_oauth2_client, auth_backend, SECRET),
    prefix="/auth/github",
    tags=["auth"],
)
api_router.include_router(
    fastapi_users.get_oauth_router(microsoft_oauth2_client, auth_backend, SECRET),
    prefix="/auth/microsoft",
    tags=["auth"],
)


@api_router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email} {user.id}"}