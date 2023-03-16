"""Main Blueprint For The App"""
from flask import Blueprint

bp = Blueprint('main_bp', __name__)

from app.main import routes