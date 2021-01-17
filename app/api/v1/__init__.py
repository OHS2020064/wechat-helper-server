#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:44
# @Author  : CoderCharm
# @File    : __init__.py.py
# @Software: PyCharm
# @Desc    :
"""

路由汇总

"""

from fastapi import APIRouter
from app.api.v1.wx import login as login
from app.api.v1.wx import message as msg
from app.api.v1.profile import profile

api_v1 = APIRouter()

api_v1.include_router(login.router, tags=["Login"])
api_v1.include_router(msg.router, tags=["Message"])
api_v1.include_router(profile.router, tags=["Profile"])
