"""Main routes for the application"""
from app.extensions import db
from app.main import bp
from app.models.category import Category
from app.models.user import User
from app.models.menu_item import MenuItem
from app.models.placed_order import PlacedOrder
from flask import render_template, request, url_for, session, redirect, flash
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
    menu_ids = [item['id'] for item in data['menu_items']]
    quantities = [int(item['quantity']) for item in data['menu_items']]
    sum_quantity = 0
    for quantity in quantities: sum_quantity += quantity
    return render_template('checkout.html',
                           menu=json.dumps(menu_ids),
                           charge=data['orderCharge'],
                           quantity=sum_quantity
                          )

@bp.route('/complete_order/', methods=['POST'])
def complete_order():
    """Completes the order made by the user"""
    pay_on_delivery = request.form.get('pay-on-delivery')
    menu_ids = json.loads(request.form.get('menu-data'))
    user_id = request.form.get('user-id')
    charge = request.form.get('total-charge')
    quantity = request.form.get('total-quantity')

    if pay_on_delivery:
        # print({
        #     'pay-on-delivery': pay_on_delivery,
        #     'menu-ids': menu,
        #     'user-id': user_id,
        #     'charge': charge,
        #     'quantity': quantity,
        # })

        buyer = User.query.get(user_id)
        new_order = PlacedOrder(quantity=quantity,
                                delivery_address=buyer.address,
                                total_price=float(charge),
                                buyer=buyer)
        for item_id in menu_ids:
            item = MenuItem.query.get(item_id)
            new_order.menu.append(item) # Appends item to order
        
        # Adds the new order to the database
        db.session.add(new_order)
        db.session.commit()
        flash('Order Placed Successfully')
        return redirect(url_for('main_bp.index'))
    else:
        flash('You Must Select A Payment Method') 
        return redirect(url_for('main_bp.checkout'))
