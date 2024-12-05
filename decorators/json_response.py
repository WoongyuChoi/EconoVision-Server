from functools import wraps
from flask import Response
import json


def json_utf8_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result, status_code = func(*args, **kwargs)
        return Response(
            json.dumps(result, ensure_ascii=False),
            mimetype="application/json",
            status=status_code,
        )

    return wrapper
