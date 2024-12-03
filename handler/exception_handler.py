from flask import jsonify
from werkzeug.exceptions import HTTPException


def register_exception_handlers(app):
    @app.errorhandler(ValueError)
    def handle_value_error(e):
        app.logger.error(f"ValueError: {str(e)}")
        return jsonify({"error": "Invalid input provided."}), 400

    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        app.logger.error(f"HTTPException: {str(e)}")
        return (
            jsonify({"error": "A server error occurred. Please try again later."}),
            e.code,
        )

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500
