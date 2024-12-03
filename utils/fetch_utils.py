import requests

from models import APIParams


def fetch_data(url, timeout=10, encoding="utf-8", return_json=True):
    """
    공통 API 호출 함수.
    :param url: API 요청 URL
    :param timeout: 요청 타임아웃 (기본값: 10초)
    :param encoding: 응답 인코딩 (기본값: utf-8)
    :param return_json: JSON 데이터를 반환할지 여부 (기본값: True)
    :return: JSON 데이터 또는 HTTP 데이터
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.encoding = encoding
        response.raise_for_status()

        if return_json:
            return response.json()
        return response
    except requests.RequestException as e:
        raise ValueError(f"Failed to fetch data from API: {e}")


def generate_statistic_url(params: APIParams) -> str:
    if not params.api_key:
        raise ValueError("API key is missing.")

    if not params.start_date or not params.end_date:
        raise ValueError("Start date and end date are required.")

    return (
        f"{params.base_url}/{params.service_name}/{params.api_key}/"
        f"{params.response_format}/{params.language}/{params.start_count}/"
        f"{params.end_count}/{params.table_code}/{params.period}/"
        f"{params.start_date}/{params.end_date}/{params.item_code}"
    )
