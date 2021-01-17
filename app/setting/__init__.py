#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:37
# @Author  : CoderCharm
# @File    : __init__.py.py
# @Software: PyCharm
# @Desc    :
"""
配置文件
根据环境变量 区分生产开发

"""

import os
import app.setting.development_config
import app.setting.production_config

# 获取环境变量
env = os.getenv("INF_ENV", "")
if env:
    # 如果有虚拟环境 则是 生产环境
    from .production_config import api_config
else:
    # 没有则是开发环境
    from .development_config import api_config

