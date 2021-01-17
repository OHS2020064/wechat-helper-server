#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:48
# @Author  : CoderCharm
# @File    : home.py
# @Software: PyCharm
# @Desc    :
"""

"""
import json

from fastapi import APIRouter

from app.api.v1.schemas import Sentence
from app.utils import response_code

router = APIRouter()


@router.post("/messages/send", summary="发送消息")
async def send(sentence: Sentence):
    """
    情绪打分 \n
    return: 返回分数, point
    """
    from app.core.bot import bot
    bot.send_text(sentence.to_user, sentence.sentence_text)
    return response_code.resp_200(sentence.to_user)
