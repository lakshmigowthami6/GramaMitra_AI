from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({
            "error": "Bad Request",
            "message": str(e.description) if hasattr(e, "description") else "చెల్లని అభ్యర్థన (Invalid request parameters).",
            "status": 400
        }), 400

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({
            "error": "Not Found",
            "message": "కోరిన సమాచారం అందుబాటులో లేదు (The requested resource was not found).",
            "status": 404
        }), 404

    @app.errorhandler(429)
    def ratelimit_exceeded(e):
        return jsonify({
            "error": "Too Many Requests",
            "message": "దయచేసి కొద్దిసేపు ఆగి మళ్ళీ ప్రయత్నించండి (Please wait a moment and try again).",
            "status": 429
        }), 429

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({
            "error": "Internal Server Error",
            "message": "సిస్టమ్ తాత్కాలిక సమస్యను ఎదుర్కొంటోంది. దయచేసి కాసేపటి తర్వాత ప్రయత్నించండి (A system error occurred. Please try again shortly).",
            "status": 500
        }), 500
