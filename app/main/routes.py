"""Main routes for the application"""
from app.main import bp
from app.models.category import Category
from flask import render_template, request
import json


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

@bp.route('/checkout/')
def checkout():
    """Handles What Happens In Checkout"""
    menu_item_str = request.args.get('items')
    total_price = request.args.get('totalPrice')
    # menu_item_dict = json.loads(menu_item_str)
    return render_template('checkout.html',
                           menu_item_dict=menu_item_str,
                           total_price=float(total_price))
