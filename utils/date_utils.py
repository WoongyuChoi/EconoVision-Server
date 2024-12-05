from datetime import datetime, timedelta
import calendar


def get_first_day_of_last_month():
    """
    지난달의 첫날(yyyyMMdd)을 반환합니다.
    """
    today = datetime.today()
    last_day_of_last_month = today.replace(day=1) - timedelta(days=1)
    first_day_of_last_month = last_day_of_last_month.replace(day=1)
    return first_day_of_last_month.strftime("%Y%m%d")


def get_last_day_of_last_month():
    """
    지난달의 마지막 날(yyyyMMdd)을 반환합니다.
    """
    today = datetime.today()
    last_day_of_last_month = today.replace(day=1) - timedelta(days=1)
    return last_day_of_last_month.strftime("%Y%m%d")


def get_first_month_of_last_year():
    """
    지난 해의 첫 달(yyyyMM)을 반환합니다.
    """
    today = datetime.today()
    first_month = today.replace(year=today.year - 1, month=1, day=1)
    return first_month.strftime("%Y%m")


def get_last_month_of_last_year():
    """
    지난 해의 마지막 달(yyyyMM)을 반환합니다.
    """
    today = datetime.today()
    last_month = today.replace(year=today.year - 1, month=12, day=1)
    return last_month.strftime("%Y%m")
