from api.server import create_app

app = create_app()


def handler(event, context):
    from werkzeug.wrappers import Request, Response

    request = Request(event)
    response = Response.from_app(app, request.environ)

    return {
        "statusCode": response.status_code,
        "headers": dict(response.headers),
        "body": response.get_data(as_text=True),
    }
