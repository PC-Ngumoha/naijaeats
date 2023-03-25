"""Main routes for the application"""
from app.restaurant import bp
from flask import render_template





@bp.route("/restaurant_register/")
def register():
    return render_template('restaurant_register.html')


@bp.route("/restaurant_login/")
def login():
    return render_template('restaurant_login.html')