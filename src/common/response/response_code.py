#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :response_code.py
# @Author   :Lowell
# @Time     :2023/8/2 13:38
from enum import Enum


class CustomCode(Enum):
    """
    自定义错误码
    """

    CAPTCHA_ERROR = (40001, "验证码错误")

    @property
    def code(self):
        """
        获取错误码
        """
        return self.value[0]

    @property
    def msg(self):
        """
        获取错误码信息
        """
        return self.value[1]
