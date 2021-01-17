#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 11:33
# @Author  : CoderCharm
# @File    : schemas.py
# @Software: PyCharm
# @Desc    :
"""

验证参数

"""
from typing import Optional

from pydantic import BaseModel


class Sentence(BaseModel):
    """
    待分析的句子  \n
    sentence_text: 默认为"" \n
    """
    to_user: list = []
    sentence_text: list = []


class UserLogin(BaseModel):
    """
    用户登录
    """
    username: str
    password: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
