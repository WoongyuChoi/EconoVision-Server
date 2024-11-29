from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello, Vercel!")


@app.route("/favicon.ico")
def favicon():
    return "", 204


def handler(event, context):
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    from werkzeug.wrappers import Request, Response

    dispatcher = DispatcherMiddleware(app)
    request = Request(event)
    response = Response.from_app(dispatcher, request.environ)
    return response(environ=None, start_response=lambda *args: None)
