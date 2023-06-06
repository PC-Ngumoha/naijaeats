"""Main routes for the application"""
from app.extensions import db
from app.main import bp
from app.models.category import Category
from app.models.user import User
from app.models.menu_item import MenuItem
from app.models.placed_order import PlacedOrder
from datetime import datetime
from flask import render_template, request, url_for, session, redirect, flash
from flask_login import login_required, current_user
import json


@bp.route('/')
@bp.route('/home/<previous>')
def index(previous=False):
    """Home page"""
    if current_user.is_anonymous and not previous:
        return redirect(url_for('main_bp.about'))
    categories = Category.query.all()
    return render_template('home.html', categories=categories)

@bp.route('/welcome/')
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
        buyer = User.query.get(user_id)
        new_order = PlacedOrder(quantity=quantity,
                                delivery_address=buyer.address,
                                total_price=float(charge),
                                buyer=buyer)
        for item_id in menu_ids:
            item = MenuItem.query.get(item_id)
            new_order.menu.append(item)
        
        # Adds the new order to the database
        db.session.add(new_order)
        db.session.commit()
        flash('Order Placed Successfully')
        return redirect(url_for('main_bp.index'))
    else:
        flash('You Must Select A Payment Method') 
        return redirect(url_for('main_bp.checkout'))
    
@bp.route('/cancel_order/<order_id>')
def cancel_order(order_id):
    """Implements Order cancellation functionality"""
    order = PlacedOrder.query.get(order_id)
    order.cancelled = True
    db.session.add(order)
    db.session.commit()
    flash('Order Cancelled Successfully')
    return redirect(url_for('user_bp.profile', user_id=current_user.id))

@bp.route('/fulfill_order/<order_id>')
def fulfill_order(order_id):
    """Implements Order fulfillment functionality"""
    order = PlacedOrder.query.get(order_id)
    order.delivered = True
    order.delivery_date = datetime.now()
    db.session.add(order)
    db.session.commit()
    flash(f'Order {order.id} Has Been Fulfilled')
    return redirect(url_for('user_bp.profile', user_id=current_user.id))

@bp.route('/delete_menuitem/<item_id>')
def delete_menuitem(item_id):
    """Deletes the specified menu item"""
    # print(item_id)
    menu_item = MenuItem.query.get(item_id)
    db.session.delete(menu_item)
    db.session.commit()
    flash(f'MenuItem \'{menu_item.title}\' Has Been Successfully Deleted')
    return redirect(url_for('user_bp.profile', user_id=current_user.id))
