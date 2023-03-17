"""Main routes for the application"""
from app.main import bp
from flask import render_template


@bp.route('/')
@bp.route('/home/')
def home_page():
    """Home page"""
    return render_template('home.html')

@bp.route('/about/')
def about_page():
    """About page"""
    return render_template('about.html')
