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
