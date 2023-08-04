#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :path_config.py
# @Author   :Lowell
# @Time     :2023/8/2 14:02
import os
from pathlib import Path

from src.core.config import settings

# 获取项目根目录
# 或使用绝对路径，指到src目录为止
BasePath = Path(__file__).resolve().parent.parent

# 日志文件路径
LogPath = os.path.join(BasePath, 'log')

