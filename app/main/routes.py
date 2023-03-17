"""Main routes for the application"""
from app.main import bp
from flask import render_template


@bp.route('/')
@bp.route('/home/')
def index():
    """Home page"""
    return render_template('home.html')

@bp.route('/about/')
def about():
    """About page"""
    return render_template('about.html')
