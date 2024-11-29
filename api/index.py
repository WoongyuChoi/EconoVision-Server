from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello, Vercel!")


def handler(event, context):
    from werkzeug.wrappers import Request, Response

    request = Request(event)
    response = Response.from_app(app, request.environ)
    return response(environ=None, start_response=None)
