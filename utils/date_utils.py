from datetime import datetime, timedelta
import calendar


def get_first_day_of_last_month():
    """
    지난달의 첫날을 반환합니다.
    :return: 지난달의 첫날 (YYYYMMDD 형식)
    """
    today = datetime.today()
    last_day_of_last_month = today.replace(day=1) - timedelta(days=1)
    first_day_of_last_month = last_day_of_last_month.replace(day=1)
    return first_day_of_last_month.strftime("%Y%m%d")


def get_last_day_of_last_month():
    """
    지난달의 마지막 날을 반환합니다.
    :return: 지난달의 마지막 날 (YYYYMMDD 형식)
    """
    today = datetime.today()
    last_day_of_last_month = today.replace(day=1) - timedelta(days=1)
    return last_day_of_last_month.strftime("%Y%m%d")
