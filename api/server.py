import time

from flask import jsonify, request

from api.external import check_ecos, fetch_exchange_rate
from api import cache


def register_routes(app):

    @app.route("/")
    def health_check():
        app.logger.info("Health check called.")
        status = {
            "status": "UP",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "details": {"ecos_api": "UP" if check_ecos() else "DOWN"},
        }
        return jsonify(status), 200

    @app.route("/favicon.<ext>")
    def favicon(ext):
        app.logger.debug(f"Favicon request received with extension: {ext}")
        return "", 204, {"Content-Type": "image/x-icon"}

    @app.route("/api/exchange-rate", methods=["GET"])
    @cache.cached(query_string=True)
    def get_exchange_rate():
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        item_code = request.args.get("item_code", "0000001")

        data = fetch_exchange_rate(start_date, end_date, item_code)
        app.logger.info("Exchange rate data fetched successfully.")
        return jsonify(data), 200
