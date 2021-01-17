# -*- coding: utf-8 -*-
import os

import itchat
import json
import base64

from app.extensions import logger
from app.setting import api_config
from app.utils import config_utils, datetime_utils


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    logger.info('personal received: %s' % json.dumps(msg))
    # itchat.send('%s' % get_response(msg['Text']), msg['FromUserName'])


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    if msg.type == 'Picture':
        path = ''  # settings.CACHE_DIR + '/' + msg.fileName
        msg.download(path)
        type_symbol = {
            'Picture': 'img',
            'Video': 'vid'}.get(msg.type, 'fil')
        base64_data = base64_image(path)
        # itchat.send('%s' % reply, msg['FromUserName'])


@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    # itchat.get_contract()
    # itchat.send('很高兴见到你!', msg['RecommendInfo']['UserName'])


@itchat.msg_register('Text', 'Picture', isGroupChat=True)
def group_reply(msg):
    msg = json.dumps(msg)
    msg = json.loads(msg)
    logger.info('group received: %s' % json.dumps(msg, ensure_ascii=False))
    config_path = os.path.join(os.path.abspath('./'), 'app', 'core', 'bot', 'config.ini')
    secret = 'b21f1338ee0467ff'
    from_user = msg['FromUserName']
    config_utils.config_get(config_path, 'from_user', '')
    if secret in msg['Text']:
        config_utils.config_set(
            config_path,
            'from_user', {'name': from_user,
                          'value': '%s %s' % (datetime_utils.current_datetime(format_string='%Y/%m/%d%H:%M:%S'), secret)})
    else:
        config_utils.config_set(
            config_path,
            'from_user', {'name': from_user,
                          'value': datetime_utils.current_datetime(format_string='%Y/%m/%d%H:%M:%S')})
    # if 'isAt' in msg:
    #     # if msg['User']['Self']['NickName'] is not settings.BOT_NAME:
    #     #         #     return
    #
    #     all_msg = msg['Content']
    #
    #     if all_msg is '':
    #         return
    #
    #     half_msg = all_msg.replace('@' + msg['User']['Self']['NickName'], '')
    #     half_msg = half_msg.replace('@' + settings.BOT_NAME, '')
    #     half_msg = half_msg.lstrip()
    #     time.sleep(1)
    #     reply = baidu_api.get_response(half_msg, msg['ActualUserName'])
    #     reply.replace('<USER-NAME>', msg['ActualNickName'])
    #     itchat.send(u'@%s %s' % (msg['ActualNickName'], reply), msg['FromUserName'])


def base64_image(file_dir):
    # 图片编码为base64
    with open(file_dir, 'rb') as fin:
        image_data = fin.read()
        base64_data = base64.b64encode(image_data)
        return base64_data


def qr_complete(uuid, status, qrcode):
    logger.info(uuid)
    logger.info(status)
    # config_path = os.path.join(os.path.abspath('./'), 'app', 'core', 'bot', 'config.ini')
    # config_utils.config_set(config_path, 'login', {'name': 'qr_code', 'value': qrcode})
    api_config.qr_code = qrcode


def send_text(to_user, content):
    for i, content in enumerate(content):
        for user in to_user:
            itchat.send(u'%s' % content, toUserName=user)
    pass
