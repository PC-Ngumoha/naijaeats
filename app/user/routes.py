"""Main routes for the application"""
from app.user import bp
from flask import render_template, redirect, url_for, request, jsonify





@bp.route("/register/", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle the signup request here
        # Essentially, we just want to create a new user at this point
        is_business = request.form.get('is_business')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        org_name = request.form.get('org_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        remember = request.form.get('remember')

        display_dict = {
            'first_name': first_name,
            'last_name': last_name,
            'org_name': org_name,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'is_business': is_business,
            'remember': remember,
        }
        
        return jsonify(display_dict)

    return render_template('register.html')


@bp.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle the login request here
        is_business = request.form.get('is_business')
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('remember')

        display_dict = {
            'email': email,
            'password': password,
            'is_business': is_business,
            'remember': remember,
        }

        return jsonify(display_dict)

    return render_template('login.html')

@bp.route("/logout/")
def logout():
    """Handle user logout here"""
    pass
