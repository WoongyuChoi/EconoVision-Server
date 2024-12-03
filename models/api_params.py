import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class APIParams:
    base_url: str = "https://ecos.bok.or.kr/api"
    service_name: Optional[str] = None
    api_key: str = os.getenv("ECOS_API_KEY")
    response_format: str = "json"
    language: str = "kr"
    start_count: int = 1
    end_count: int = 10000
    table_code: Optional[str] = None
    period: str = "D"
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    item_code: Optional[str] = None
