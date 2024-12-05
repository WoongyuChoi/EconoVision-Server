import inspect
from functools import wraps

from utils import (
    get_first_day_of_last_month,
    get_first_month_of_last_year,
    get_last_day_of_last_month,
    get_last_month_of_last_year,
)


def default_params(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_signature = inspect.signature(func)
        func_params = func_signature.parameters

        if "start_date" in func_params:
            kwargs["start_date"] = (
                kwargs.get("start_date") or get_first_day_of_last_month()
            )
        if "end_date" in func_params:
            kwargs["end_date"] = kwargs.get("end_date") or get_last_day_of_last_month()
        if "start_month" in func_params:
            kwargs["start_month"] = (
                kwargs.get("start_month") or get_first_month_of_last_year()
            )
        if "end_month" in func_params:
            kwargs["end_month"] = (
                kwargs.get("end_month") or get_last_month_of_last_year()
            )

        return func(*args, **kwargs)

    return wrapper
