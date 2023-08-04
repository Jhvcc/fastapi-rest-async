#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :models.py
# @Author   :Lowell
# @Time     :2023/8/2 11:12
from typing import List

from beanie import Document
from fastapi_users.db import BaseOAuthAccount, BeanieBaseUser
from pydantic import Field


class OAuthAccount(BaseOAuthAccount):
    pass


class User(BeanieBaseUser, Document):
    oauth2_accounts: List[OAuthAccount] = Field(default_factory=list)

