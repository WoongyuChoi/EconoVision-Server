from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello, Vercel!")


def handler(request, context=None):
    return app(request.environ, start_response=lambda *args: None)
