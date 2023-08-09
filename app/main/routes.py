"""Main routes for the application"""
from app.extensions import db
from app.main import bp
from app.models.category import Category
from app.models.user import User
from app.models.menu_item import MenuItem
from app.models.placed_order import PlacedOrder
from datetime import datetime
from flask import render_template, request, url_for, session, redirect, flash, abort,\
    Response
from flask_login import login_required, current_user
import json


@bp.route('/')
@bp.route('/home/<previous>')
def index(previous=False):
    """Home page"""
    # if current_user.is_anonymous and not previous:
    #     return redirect(url_for('main_bp.about'))
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

@bp.route('/compose/', methods=['GET', 'POST'])
def compose_menuitem():
    """Enables creation of new menu-item"""
    if request.method == 'POST':
        # Gets the other data from the user
        if not request.form.get('title'):
            flash('MenuItem must have a title')
            return redirect(url_for('main_bp.compose_menuitem'))
        title = request.form.get('title')
        if not request.form.get('price'):
            flash('MenuItem must have a set price')
            return redirect(url_for('main_bp.compose_menuitem'))
        price = float(request.form.get('price'))
        if not request.form.get('categories'):
            flash('MenuItem must belong to one of the specified categories')
            return redirect(url_for('main_bp.compose_menuitem'))
        category = Category.query.get(request.form.get('categories'))
        description = request.form.get('description')
        restaurant = User.query.get(current_user.id)
        # Handles file inputs
        image = request.files['image']
        if not image or image.filename == '':
            flash('You have to upload an image')
            return redirect(url_for('main_bp.compose_menuitem'))
        # print({title, price, description, image, category, restaurant})
        
        # Creates new menu item here
        item = MenuItem(
            title=title,
            price=price,
            description=description,
            image=image.read(),
            mimetype=image.mimetype,
            category=category,
            restaurant=restaurant
        )
        # Performs the initial saving of the item so we can get
        # it's id
        db.session.add(item)
        db.session.commit()
        # Set the image_url on that particular item to the image
        # # we just set up
        item.image_url = f'/menu_item/{item.id}'
        db.session.add(item)
        db.session.commit()
        flash('New menu item created successfully')
        return redirect(url_for('user_bp.profile', user_id=current_user.id))
    categories = Category.query.all()
    return render_template('compose.html', categories=categories)

@bp.route('/modify/<item_id>', methods=['GET', 'POST'])
def modify_menuitem(item_id):
    """Modifies a preexisting menu-item"""
    if request.method == 'POST':
        # print(request.form)
        # print(request.files['image'])
        if not request.form.get('title'):
            flash('MenuItem must have a title')
            return redirect(url_for('main_bp.compose_menuitem'))
        title = request.form.get('title')
        if not request.form.get('price'):
            flash('MenuItem must have a set price')
            return redirect(url_for('main_bp.compose_menuitem'))
        price = float(request.form.get('price'))
        if not request.form.get('categories'):
            flash('MenuItem must belong to one of the specified categories')
            return redirect(url_for('main_bp.compose_menuitem'))
        category = Category.query.get(request.form.get('categories'))
        description = request.form.get('description')
        restaurant = User.query.get(current_user.id)
        # Handles file inputs
        image = request.files['image']
        if not image or image.filename == '':
            flash('You have to upload an image')
            return redirect(url_for('main_bp.compose_menuitem'))

        item = MenuItem.query.get(item_id)
        item.title = title
        item.price = price
        item.description = description
        item.category = category
        item.restaurant = restaurant
        item.image = image.read()
        item.mimetype = image.mimetype
        item.image_url = f'/menu_item/{item.id}'

        db.session.add(item)
        db.session.commit()

        flash(f'MenuItem {item.title} modified successfully')
        return redirect(url_for('user_bp.profile', user_id=current_user.id))
    item = MenuItem.query.get(item_id)
    categories = Category.query.all()
    return render_template('compose.html', categories=categories, item=item)

@bp.route('/menu_item/<menu_id>')
def get_menuitem_image(menu_id):
    """returns the menu_item image"""
    item = MenuItem.query.get(menu_id)
    # If such item does not exist, abort
    if not item:
        return abort(404)
    # Returns image
    return Response(item.image, mimetype=item.mimetype)
