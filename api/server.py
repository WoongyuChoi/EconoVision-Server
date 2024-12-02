import time

from flask import Flask, jsonify, request

from api.external import check_ecos, fetch_exchange_rate
from handler.logger import get_logger

app = Flask(__name__)
logger = get_logger(__name__)


@app.route("/")
def health_check():
    status = {
        "status": "UP",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "details": {"ecos_api": "UP" if check_ecos() else "DOWN"},
    }
    return jsonify(status), 200


@app.route("/favicon.<ext>")
def favicon(ext):
    return "", 204, {"Content-Type": "image/x-icon"}


@app.route("/api/exchange-rate", methods=["GET"])
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

    start_time = time.time()
    logger.info(f"Request: {event.get('httpMethod')} {event.get('path')}")
    # logger.debug(f"Headers: {event.get('headers')}")
    # logger.debug(f"Query Parameters: {event.get('queryStringParameters')}")
    # logger.debug(f"Body: {event.get('body')}")

    request = Request(event)
    response = Response.from_app(app, request.environ)

    duration = time.time() - start_time
    logger.info(
        f"Response: {response.status_code} {dict(response.headers)} "
        f"{response.get_data(as_text=True)} Duration: {duration:.2f}s"
    )

    return {
        "statusCode": response.status_code,
        "headers": dict(response.headers),
        "body": response.get_data(as_text=True),
    }
