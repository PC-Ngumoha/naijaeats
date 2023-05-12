"""Main routes for the application"""
from app.user import bp
from flask import render_template





@bp.route("/register/")
def register():
    return render_template('register.html')


@bp.route("/login/")
def login():
    return render_template('login.html')