#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :routers.py
# @Author   :Lowell
# @Time     :2023/8/2 11:33
from fastapi import APIRouter

from .auth.routers import api_router as auth_router
from ..core.config import settings

api_router = APIRouter(prefix=settings.API_V1_STR)

api_router.include_router(auth_router)

