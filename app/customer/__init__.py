"""Main Blueprint For The App"""
from flask import Blueprint



bp = Blueprint('customer_bp', __name__)

from app.customer import routes