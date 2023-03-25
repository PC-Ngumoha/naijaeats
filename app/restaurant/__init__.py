"""Main Blueprint For The App"""
from flask import Blueprint

bp = Blueprint('restaurant_bp', __name__)

from app.restaurant import routes