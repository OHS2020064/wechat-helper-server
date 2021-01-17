#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 14:47
# @Author  : CoderCharm
# @File    : development_config.py
# @Software: PyCharm
# @Desc    :
"""

开发环境配置

"""
import os
from typing import Union, Optional
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):
    #
    HOST: str = "127.0.0.1"
    #
    PORT: int = 8010
    API_HOST: str = 'zqcp.ohsyun.com'
    URL_PREFIX: str = ''
    API_PREFIX: str = 'spider/collecter'
    # 文档地址
    DOCS_URL: str = "/wx/api/v1/docs"
    # # 文档关联请求数据接口
    OPENAPI_URL: str = "/wx/api/v1/openapi.json"
    # 禁用 redoc 文档
    REDOC_URL: Optional[str] = None

    DEBUG: bool = True

    QR_TIMEOUT: int = 15
    qr_code = ''
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = 'aeq)s(*&dWEQasd8**&^9asda_asdasd*&*&^+_sda'

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = 'root'
    MYSQL_PASSWORD: str = "Admin12345-"
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "172.16.137.129"
    MYSQL_DATABASE: str = 'Mall'

    # Mysql地址
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

    # api请求headers
    API_HEADERS = {'Content-Type': 'application/json'}
    # config address
    CONFIG_PATH = os.path.join(os.path.abspath('./'), 'app', 'setting', 'config.ini')

    def make_url(self, address, host=None, port=None, prefix='https'):
        if 'host' in os.environ:
            host = os.environ['host']
        elif host is None:
            host = self.API_HOST
        header = '%s://%s' % (prefix, host)
        if port is not None:
            header = '%s:%s' % (header, port)
        api_prefix = None
        if 'api_prefix' in os.environ:
            api_prefix = os.environ['api_prefix']
        elif api_prefix is None:
            api_prefix = self.API_PREFIX
        url = '%s/%s/%s' % (header, api_prefix, address)
        return url


api_config = Config()
