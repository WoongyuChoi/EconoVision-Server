from handler.logger import get_logger

logger = get_logger(__name__)


class DataProcessor:
    """
    외부 API에서 받은 데이터를 처리하는 클래스.
    """

    @staticmethod
    def process_exchange_rate_data(response_data):
        if "StatisticSearch" not in response_data:
            logger.error(f"ValueError: {str(response_data)}")

        raw_rows = response_data.get("StatisticSearch", {}).get("row", [])
        if not raw_rows:
            return {"content": []}

        processed_data = []
        for row in raw_rows:
            try:
                value = float(row.get("DATA_VALUE", "0").replace(",", ""))
            except ValueError:
                value = 0

            processed_data.append(
                {
                    "value": value,
                    "item_code": row.get("ITEM_CODE1"),
                    "item_name": row.get("ITEM_NAME1"),
                    "time": row.get("TIME"),
                    "unit": (
                        row.get("UNIT_NAME").strip() if row.get("UNIT_NAME") else None
                    ),
                }
            )

        sorted_data = sorted(
            processed_data,
            key=lambda x: x["time"] if x["time"] else "",
            reverse=False,
        )

        return {"content": sorted_data}
