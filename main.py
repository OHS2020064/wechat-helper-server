#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:36
# @Author  : CoderCharm
# @File    : main.py
# @Software: PyCharm
# @Desc    :
"""

pip install uvicorn

"""
import os

import app.api
import app.core
import app.extensions
import app.setting
import app.utils

import pydantic.dataclasses
import pydantic.version
import pydantic.color
import colorsys
import pydantic.types
import pydantic.validators
import pydantic.datetime_parse
import pydantic.main
import pydantic.parse
import pydantic.networks
import pydantic.decorator
import pydantic.env_settings
import pydantic.tools

import passlib
import passlib.handlers.bcrypt

from app.api import create_app
from app.setting import api_config
from app.utils import config_utils

app = create_app()


def run_production():
    import asyncio
    import uvloop
    from hypercorn.asyncio import serve
    from hypercorn.config import Config

    config = Config()
    config.bind = ['%s:%s' % (api_config.HOST, api_config.PORT)]

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(serve(app, config))
    pass


def run_development():
    import uvicorn
    uvicorn.run(app='main:app', host=api_config.HOST, port=api_config.PORT, workers=1, reload=True, debug=False)
    pass


# sys.setrecursionlimit(3000)  # 将默认的递归深度修改为3000

if __name__ == "__main__":
    # 获取环境变量
    env = os.getenv("INF_ENV", "")
    if env:
        run_production()
    else:
        run_development()
