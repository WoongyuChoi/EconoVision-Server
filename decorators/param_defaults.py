from functools import wraps
from utils import get_first_day_of_last_month, get_last_day_of_last_month


def default_params(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs["start_date"] = kwargs.get("start_date") or get_first_day_of_last_month()
        kwargs["end_date"] = kwargs.get("end_date") or get_last_day_of_last_month()
        return func(*args, **kwargs)

    return wrapper
