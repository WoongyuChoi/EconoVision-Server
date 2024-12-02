import time

from flask import Flask, jsonify, request
from flask_caching import Cache

from api.external import check_ecos, fetch_exchange_rate
from config import Config
from handler.logger import get_logger

app = Flask(__name__)
app.config.from_object(Config)

cache = Cache(app)

logger = get_logger(__name__)


@app.route("/")
def health_check():
    logger.info("Health check called.")
    status = {
        "status": "UP",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "details": {"ecos_api": "UP" if check_ecos() else "DOWN"},
    }
    return jsonify(status), 200


@app.route("/favicon.<ext>")
def favicon(ext):
    logger.debug(f"Favicon request received with extension: {ext}")
    return "", 204, {"Content-Type": "image/x-icon"}


@app.route("/api/exchange-rate", methods=["GET"])
@cache.cached(query_string=True)
def get_exchange_rate():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    item_code = request.args.get("item_code", "0000001")

    logger.debug(
        f"Parameters received: start_date={start_date}, end_date={end_date}, item_code={item_code}"
    )

    try:
        data = fetch_exchange_rate(start_date, end_date, item_code)
        logger.info("Exchange rate data fetched successfully.")
        return jsonify(data), 200
    except ValueError as e:
        logger.error(f"Error fetching exchange rate: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500


def handler(event, context):
    from werkzeug.wrappers import Request, Response

    request = Request(event)
    response = Response.from_app(app, request.environ)

    return {
        "statusCode": response.status_code,
        "headers": dict(response.headers),
        "body": response.get_data(as_text=True),
    }
