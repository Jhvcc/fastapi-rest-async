#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :schemas.py
# @Author   :Lowell
# @Time     :2023/8/2 11:15
from beanie import PydanticObjectId
from fastapi_users import schemas


class BaseUser(schemas.BaseUser[PydanticObjectId]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
