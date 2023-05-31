"""Main routes for the application"""
from app.main import bp
from app.models.category import Category
from app.models.user import User
from app.models.menu_item import MenuItem
from flask import render_template, request, url_for, session, redirect
from flask_login import login_required
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
@login_required
def display_category(cat_id):
    """Displays a specific category of items"""
    category = Category.query.get(cat_id)
    return render_template('category.html', category=category)

@bp.route('/checkout/', methods=['GET', 'POST'])
def checkout():
    """Handles What Happens In Checkout"""
    # menu_item_str = request.args.get('items')
    # total_price = request.args.get('totalPrice')
    # menu_item_dict = json.loads(menu_item_str)
    if request.method == 'POST':
        request_body = request.json
        session['data'] = request_body
        return redirect(url_for('main_bp.checkout'))
    
    data = session.get('data', {})
    return render_template('checkout.html', data=data)
