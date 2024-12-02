import os

import requests
from dotenv import load_dotenv

from handler.logger import get_logger
from util.date_utils import get_first_day_of_last_month, get_last_day_of_last_month

logger = get_logger(__name__)

if os.getenv("VERCEL_ENV") is None:
    load_dotenv()


def check_ecos():
    url = "https://ecos.bok.or.kr/api/"

    try:
        response = requests.get(url, timeout=10)
        logger.info(f"Response: {response.status_code} {dict(response.headers)} ")
        return response.status_code == 200
    except requests.RequestException:
        return False


def fetch_exchange_rate(start_date=None, end_date=None, item_code="0000001"):
    """
    외부 API를 호출하여 주요국 통화의 대원화환율 데이터를 조회합니다.
    :param start_date: 검색 시작일자 (YYYYMMDD), 기본값은 지난달의 첫날
    :param end_date: 검색 종료일자 (YYYYMMDD), 기본값은 지난달의 마지막날
    :param item_code: 통계항목코드1 (기본값: 0000001, 미국 달러)
    :return: API 응답 데이터 (JSON)
    """

    if not start_date:
        start_date = get_first_day_of_last_month()
    if not end_date:
        end_date = get_last_day_of_last_month()

    base_url = "https://ecos.bok.or.kr/api"
    service_name = "StatisticSearch"
    api_key = os.getenv("ECOS_API_KEY")
    response_format = "json"
    language = "kr"
    start_count = 1
    end_count = 10000
    table_code = "731Y001"
    period = "D"

    url = f"{base_url}/{service_name}/{api_key}/{response_format}/{language}/{start_count}/{end_count}/{table_code}/{period}/{start_date}/{end_date}/{item_code}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise ValueError(f"Failed to fetch data from ECOS API: {e}")
