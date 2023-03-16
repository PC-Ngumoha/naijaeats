"""Main routes for the application"""
from app.main import bp


@bp.route('/')
@bp.route('/home/')
def home_page():
    """Home page"""
    return '<h1>Home Page</h1>'

@bp.route('/about/')
def about_page():
    """About page"""
    return '<h1>About Page</h1>'
