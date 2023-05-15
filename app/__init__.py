"""App Initialization"""
from config import Config
from flask import Flask
from flask_login import LoginManager
from app.extensions import db
from app.models.user import User


def create_app(config_class=Config):
    """Test setup for flask"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize packages here
    db.init_app(app=app)

    # Initializing the login_manager here
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user_bp.login'

    # create app blueprints here
    from app.main import bp as main_bp
    from app.user import bp as user_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)

    @login_manager.user_loader
    def load_user(user_id):
        """Loads the current user whose ID is stored in the session"""
        return User.query.get(user_id)

    @app.route('/test/')
    def test_app():
        return '<h1>It seems the app is working well</h1>'
    return app
