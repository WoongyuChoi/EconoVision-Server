from api.server import app


def handler(event, context):
    from werkzeug.wrappers import Request, Response
    from api.logger import get_logger

    logger = get_logger(__name__)

    logger.info(f"Request: {event.get('httpMethod')} {event.get('path')}")
    # logger.debug(f"Headers: {event.get('headers')}")
    # logger.debug(f"Query Parameters: {event.get('queryStringParameters')}")
    # logger.debug(f"Body: {event.get('body')}")

    request = Request(event)
    response = Response.from_app(app, request.environ)

    logger.info(f"Response: {response.status_code} {response.get_data(as_text=True)}")

    return {
        "statusCode": response.status_code,
        "headers": dict(response.headers),
        "body": response.get_data(as_text=True),
    }
