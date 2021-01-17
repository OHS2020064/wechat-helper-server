import json

import grequests

from app.extensions import logger
from app.setting import api_config


def err_handler(request, exception):
    logger.error(exception)


def get(url, headers=api_config.API_HEADERS):
    req_list = [grequests.request("GET",
                                  url=url,
                                  headers=headers,
                                  timeout=10)]
    logger.info(url)
    return grequests.imap(req_list, exception_handler=err_handler)


def post(url, item):
    req_list = [grequests.request("POST",
                                  url=url,
                                  data=json.dumps(item),
                                  headers=api_config.API_HEADERS,
                                  timeout=10)]
    logger.info(url)
    logger.info(json.dumps(item, ensure_ascii=False))
    return grequests.imap(req_list, exception_handler=err_handler)
