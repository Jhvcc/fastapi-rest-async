#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :registry.py
# @Author   :Lowell
# @Time     :2023/8/2 11:32
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.apps.routers import api_router
from src.common.exception.exception_handler import register_exception
from src.common.redis import redis_client
from src.common.task import scheduler
from src.core.config import settings
from src.database.connection import init_db
from src.utils.health_check import ensure_unique_route_names
from src.utils.openapi import simplify_operation_ids


@asynccontextmanager
async def register_init(app: FastAPI):
    """
    启动初始化
    """
    # 连接mongodb
    await init_db()

    # 连接redis
    await redis_client.open()

    # 启动定时任务
    scheduler.start()

    yield

    # 关闭 redis 连接
    await redis_client.close()

    # 关闭定时任务
    scheduler.shutdown()


def register_app():
    # FastAPI
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOCS_URL,
        openapi_url=settings.OPENAPI_URL,
        lifespan=register_init,     # https://fastapi.tiangolo.com/advanced/events/
    )

    # 静态文件
    register_static_file(app)

    # 中间件
    register_middleware(app)

    # 路由
    register_router(app)

    # 分页
    register_page(app)

    # 全局异常处理
    register_exception(app)

    return app


def register_static_file(app: FastAPI):
    """
    静态文件交互开发模式, 生产使用 nginx 静态资源服务

    :param app:
    :return:
    """
    if settings.STATIC_FILES:
        import os
        from fastapi.staticfiles import StaticFiles

        if not os.path.exists('./static'):
            os.mkdir('./static')
        app.mount('/static', StaticFiles(directory='static'), name='static')


def register_middleware(app: FastAPI):
    """
    中间件，执行顺序从下往上

    :param app:
    :return:
    """
    # Gzip
    if settings.MIDDLEWARE_GZIP:
        from fastapi.middleware.gzip import GZipMiddleware

        app.add_middleware(GZipMiddleware)
    # Access log
    # TODO: opera log 中间件完全可行时将被删除
    # if settings.MIDDLEWARE_ACCESS:
    #     from backend.app.middleware.access_middleware import AccessMiddleware
    #
    #     app.add_middleware(AccessMiddleware)
    # # Opera log
    # app.add_middleware(OperaLogMiddleware)
    # # JWT auth: Always open
    # app.add_middleware(
    #     AuthenticationMiddleware, backend=JwtAuthMiddleware(), on_error=JwtAuthMiddleware.auth_exception_handler
    # )
    # CORS: Always at the end
    if settings.MIDDLEWARE_CORS:
        from fastapi.middleware.cors import CORSMiddleware

        app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )


def register_router(app: FastAPI):
    """
    路由

    :param app: FastAPI
    :return:
    """
    # dependencies = [Depends(demo_site)] if settings.DEMO_MODE else None

    # API
    # app.include_router(v1, dependencies=dependencies)
    app.include_router(api_router)

    # Extra
    ensure_unique_route_names(app)
    simplify_operation_ids(app)


def register_page(app: FastAPI):
    """
    分页查询

    :param app:
    :return:
    """
    ...