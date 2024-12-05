from flask import request


def get_request_params(*keys, defaults=None):
    """
    요청에서 여러 파라미터를 한 번에 추출.
    :param keys: 추출할 파라미터 키들
    :param defaults: 기본값 딕셔너리 (key-value 쌍)
    :return: 추출된 파라미터 딕셔너리
    """
    if defaults is None:
        defaults = {}

    return {key: request.args.get(key, defaults.get(key)) for key in keys}
