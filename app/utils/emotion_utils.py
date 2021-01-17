import json

from app.extensions import logger
from app.setting import api_config
from app.utils import request_utils, config_utils


def except_error(e):
    logger.error('can not request emotion parameter')
    logger.error(e)
    return [0.23, 0.7, 0.8, 0.91]


def emotion_judge(points):
    data = []
    try:
        json_judge_objects = next(config_utils.config_get(api_config.CONFIG_PATH, 'judge', 'judge_points'))
    except Exception as e:
        json_judge_objects = son.dumps(except_error(e))
    if len(json_judge_objects) > 0:
        json_judge_objects = json.loads(json_judge_objects)
    else:
        judge_url = api_config.make_url('Metadata/')
        try:
            judge_point_resp = request_utils.get('%s?recode_id=emotion_judge_point' % judge_url)
            json_judge_resp = json.loads(next(judge_point_resp).content)
            json_judge_objects = json_judge_resp['data'][0]['content']
            config_utils.config_set(api_config.CONFIG_PATH, 'judge',
                                    {'name': 'judge_points', 'value': json.dumps(json_judge_objects)})
        except Exception as e:
            json_judge_objects = except_error(e)
    for point in points:
        if 0 < point <= float(json_judge_objects[0]):
            judge = 0
        elif float(json_judge_objects[0]) < point <= float(json_judge_objects[1]):
            judge = 1
        elif float(json_judge_objects[2]) < point <= float(json_judge_objects[3]):
            judge = 3
        elif float(json_judge_objects[3]) < point <= 1:
            judge = 4
        else:
            judge = 2
        data.append({'judge': judge,
                     'point': point})
    return data
