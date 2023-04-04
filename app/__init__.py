"""App Initialization"""
from config import Config
from flask import Flask
from app.extensions import db





def create_app(config_class=Config):
    """Test setup for flask"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize packages here
    db.init_app(app=app)



    # create app blueprints here
    from app.main import bp as main_bp
    from app.restaurant import bp as restaurant_bp
    from app.customer import bp as customer_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(customer_bp)


    @app.route('/test/')
    def test_app():
        return '<h1>It seems the app is working well</h1>'
    return app




