import os

from dotenv import load_dotenv

from decorators import default_params
from handler.logger import get_logger
from models import APIParams
from utils import fetch_data, generate_statistic_url

logger = get_logger(__name__)

if os.getenv("VERCEL_ENV") is None:
    load_dotenv()


class ExternalAPI:

    @staticmethod
    def check_ecos():
        try:
            response = fetch_data("https://ecos.bok.or.kr/api/", return_json=False)
            logger.info(f"Response: {response.status_code} {dict(response.headers)} ")
            return response.status_code == 200
        except ValueError as e:
            logger.warning(f"ECOS API health check failed: {e}")
            return False

    @staticmethod
    @default_params
    def fetch_exchange_rate(start_date, end_date, item_code=None):
        """
        외부 API를 호출하여 주요국 통화의 대원화환율 데이터를 조회합니다.
        :param start_date: 검색 시작일자 (YYYYMMDD), 기본값은 지난달의 첫날
        :param end_date: 검색 종료일자 (YYYYMMDD), 기본값은 지난달의 마지막날
        :param item_code: 통계항목코드1 (기본값: 0000001, 미국 달러)
        :return: API 응답 데이터 (JSON)
        """

        params = APIParams(
            service_name="StatisticSearch",
            table_code="731Y001",
            start_date=start_date,
            end_date=end_date,
            item_code=item_code or "0000001",
        )

        url = generate_statistic_url(params)
        return fetch_data(url)
