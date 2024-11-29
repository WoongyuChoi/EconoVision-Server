from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello, Vercel!")


@app.route("/favicon.ico")
def favicon():
    return "", 204


def handler(event, context):
    import logging
    from werkzeug.wrappers import Request, Response

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Incoming Request:")
    logger.info(f"HTTP Method: {event.get('httpMethod')}")
    logger.info(f"Path: {event.get('path')}")
    logger.info(f"Headers: {event.get('headers')}")
    logger.info(f"Query Parameters: {event.get('queryStringParameters')}")
    logger.info(f"Body: {event.get('body')}")

    request = Request(event)
    response = Response.from_app(app, request.environ)

    logger.info("Outgoing Response:")
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Headers: {dict(response.headers)}")
    logger.info(f"Body: {response.get_data(as_text=True)}")

    return {
        "statusCode": response.status_code,
        "headers": dict(response.headers),
        "body": response.get_data(as_text=True),
    }
