"""App Initialization"""
from config import Config
from flask import Flask


def create_app(config_class=Config):
    """Test setup for flask"""
    app = Flask(__name__)

    # Initialize db here

    # create app blueprints here

    @app.route('/test/')
    def test_app():
        return '<h1>It seems the app is working well</h1>'
    return app
