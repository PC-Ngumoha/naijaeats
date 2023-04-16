"""Definition of MenuItem DB model"""
from app.extensions import db
from app.models.placed_order import PlacedOrder
from app.utilities import generate_uuid
# from flask import url_for


class MenuItem(db.Model):
    """MenuItem DB model"""
    __tablename__ = 'menu_item'
    id = db.Column(db.String(80), primary_key=True, default=generate_uuid)
    image_url = db.Column(db.String(200),
                          default='../static/images/naijafoods.jpeg')
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(5, 2), nullable=False)
    ingredients = db.Column(db.Text)
    category_id = db.Column(db.String(80), db.ForeignKey('category.id'))
    restaurant_id = db.Column(db.String(80), db.ForeignKey('restaurant.id'))

    orders = db.relationship('PlacedOrder', backref="menu_item")

    def __repr__(self):
        """String representation of model instance"""
        return f'<MenuItem {self.id} : {self.title}>'
