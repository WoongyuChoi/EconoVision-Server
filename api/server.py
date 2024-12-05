import time

from flask import Flask, jsonify
from flask_caching import Cache

from api import ExternalAPI
from config import Config
from decorators import json_utf8_response
from handler.exception_handler import register_exception_handlers
from handler.logger import get_logger
from utils import get_request_params

app = Flask(__name__)
app.config.from_object(Config)

cache = Cache(app)
logger = get_logger(__name__)

register_exception_handlers(app)


@app.route("/")
def health_check():
    status = {
        "status": "UP",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "details": {"ecos_api": "UP" if ExternalAPI.check_ecos() else "DOWN"},
    }
    return jsonify(status), 200


@app.route("/favicon.<ext>")
def favicon(ext):
    logger.debug(f"Favicon request received with extension: {ext}")
    return "", 204, {"Content-Type": "image/x-icon"}


@app.route("/api/exchange-rate", methods=["GET"])
@json_utf8_response
@cache.cached(query_string=True)
def get_exchange_rate():
    params = get_request_params("start_date", "end_date", "item_code")

    data = ExternalAPI.fetch_exchange_rate(
        start_date=params["start_date"],
        end_date=params["end_date"],
        item_code=params["item_code"],
    )
    return data, 200


@app.route("/api/foreign-reserves", methods=["GET"])
@cache.cached(query_string=True)
@json_utf8_response
def get_foreign_reserves():
    params = get_request_params("start_month", "end_month")

    data = ExternalAPI.fetch_foreign_reserves(
        start_month=params["start_month"],
        end_month=params["end_month"],
    )
    return data, 200


def handler(event, context):
    from werkzeug.wrappers import Request, Response

    request = Request(event)
    response = Response.from_app(app, request.environ)

    return {
        "statusCode": response.status_code,
        "headers": dict(response.headers),
        "body": response.get_data(as_text=True),
    }
