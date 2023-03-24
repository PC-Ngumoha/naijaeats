"""Main routes for the application"""
from app.main import bp
from app.models.category import Category
from flask import render_template


@bp.route('/')
@bp.route('/home/')
def index():
    """Home page"""
    categories = Category.query.all()
    return render_template('home.html', categories=categories)

@bp.route('/about/')
def about():
    """About page"""
    return render_template('about.html')
