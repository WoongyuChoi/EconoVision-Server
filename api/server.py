import time
from flask import Flask, jsonify
from api.logger import get_logger

app = Flask(__name__)
logger = get_logger(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello, Vercel!")


@app.route("/favicon.ico")
def favicon():
    return "", 204, {"Content-Type": "image/x-icon"}


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
