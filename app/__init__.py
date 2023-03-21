"""App Initialization"""
from config import Config
from flask import Flask


def create_app(config_class=Config):
    """Test setup for flask"""
    app = Flask(__name__)

    # Initialize packages here

    # create app blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)


    @app.route('/test/')
    def test_app():
        return '<h1>It seems the app is working well</h1>'
    return app
