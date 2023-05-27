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

@bp.route('/category/<cat_id>')
def display_category(cat_id):
    """Displays a specific category of items"""
    category = Category.query.get(cat_id)
    return render_template('category.html', category=category)
