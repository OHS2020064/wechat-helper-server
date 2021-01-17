#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:48
# @Author  : CoderCharm
# @File    : home.py
# @Software: PyCharm
# @Desc    :
"""

"""
import os
import threading
import time

import itchat
from fastapi import APIRouter

from app.core.bot import bot
from app.setting import api_config
from app.utils import response_code, config_utils

router = APIRouter()


class LoginThread(threading.Thread):

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        qr_path = os.path.join(os.path.abspath('./'), 'app', 'core', 'bot', 'qr.png')
        itchat.auto_login(picDir=qr_path, qrCallback=bot.qr_complete)
        itchat.run()
        print("Exiting " + self.name)


@router.get("/user/login", summary="登录微信")
async def login():
    """
    登录微信 \n
    return: 二维码, point
    """
    api_config.qr_code = ''
    config_path = os.path.join(os.path.abspath('./'), 'app', 'core', 'bot', 'config.ini')
    config_utils.config_clean(config_path, 'from_user')
    itchat.logout()
    child_thread = LoginThread(1, "Thread-1", 1)
    child_thread.start()

    time_out = 0
    while True and time_out <= api_config.QR_TIMEOUT:
        time.sleep(1)

        if api_config.qr_code != '':
            break
        time_out += 1
    return response_code.resp_file(api_config.qr_code)


@router.get("/user/users", summary="微信好友列表")
async def login():
    config_path = os.path.join(os.path.abspath('./'), 'app', 'core', 'bot', 'config.ini')
    return response_code.resp_200(config_utils.all_options(config_path, 'from_user'))


@router.get("/user/subscribes", summary="已订阅好友列表")
async def login():
    config_path = os.path.join(os.path.abspath('./'), 'app', 'core', 'bot', 'config.ini')
    items, conf = config_utils.all_options(config_path, 'from_user')
    subscribes = []
    secret = 'b21f1338ee0467ff'
    for item in items:
        print(item)
        if secret not in item[1]:
            continue
        subscribes.append(item[0])
    return response_code.resp_200(subscribes)
