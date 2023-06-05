"""Main routes for the application"""
from app.user import bp
from app.extensions import db
from app.models.city import City
from app.models.menu_item import MenuItem
from app.models.user import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


@bp.route("/register/", methods=['GET', 'POST'])
def register():
    """Handles user registration attempts"""
    if request.method == 'POST':
        is_business = request.form.get('is_business')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        org_name = request.form.get('org_name')
        city_name = request.form.get('city_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('User with that email already exists')
            return redirect(url_for('user_bp.register'))
        
        city = City.query.filter_by(name=city_name).first()
        if not city:
            flash('We do not deliver to specified city')
            return redirect(url_for('user_bp.register'))

        if password != confirm_password:
            flash('Something is wrong with the password you entered')
            return redirect(url_for('user_bp.register'))
        
        user = User(
            is_business=is_business,
            first_name=first_name,
            last_name=last_name,
            org_name=org_name,
            email=email,
            password=generate_password_hash(password),
            city=city
        )
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('user_bp.login'))

    return render_template('register.html')


@bp.route("/login/", methods=['GET', 'POST'])
def login():
    """Handles user login attempts"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('remember')

        found_user = User.query.filter_by(email=email).first()
        if not found_user:
            flash('User does not exist, register first')
            return redirect(url_for('user_bp.login'))

        if not check_password_hash(found_user.password, password):
            flash('Password is incorrect')
            return redirect(url_for('user_bp.login'))
        
        login_user(found_user, remember=remember)
        return redirect(url_for('main_bp.index'))

    return render_template('login.html')

@bp.route("/logout/")
def logout():
    """Handle user logout here"""
    logout_user()
    return redirect(url_for('main_bp.index'))

@bp.route("/profile/<user_id>")
@login_required
def profile(user_id):
    """Displays the user's profile"""
    user = User.query.get(user_id)
    if user.is_business:
        orders = []
        menu = MenuItem.query.all()
        for menu_item in menu:
            if menu_item.restaurant == user:
                orders.extend(menu_item.orders)
    else:
        orders = user.orders
    return render_template('profile.html', user=user, orders=orders)
