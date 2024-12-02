import requests
from api.logger import get_logger

logger = get_logger(__name__)


def check_ecos():
    url = "https://ecos.bok.or.kr/api/"
    try:
        response = requests.get(url, timeout=5)
        logger.info(f"Response: {response.status_code} {dict(response.headers)} ")
        return response.status_code == 200
    except requests.RequestException:
        return False
