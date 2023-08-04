#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :openapi.py
# @Author   :Lowell
# @Time     :2023/8/2 11:48
from fastapi import FastAPI
from fastapi.routing import APIRoute


def simplify_operation_ids(app: FastAPI) -> None:
    """
    简化操作 ID，以便生成的客户端具有更简单的 api 函数名称

    :param app:
    :return:
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name
