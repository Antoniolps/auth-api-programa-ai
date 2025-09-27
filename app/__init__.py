from flask import Flask, jsonify
from .extensions import init_extensions
from .routes import bp as users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    init_extensions(app)

    @app.route('/')
    def health():
        return jsonify({"status": "I'm running"})

    app.register_blueprint(users_bp)

    return app