"""Description of PlacedOrder DB model"""
from app.extensions import db
from app.models.review import Review
from app.utilities import generate_uuid
from sqlalchemy.sql import func


class PlacedOrder(db.Model):
    """PlacedOrder DB model"""
    __tablename__ = 'placed_order'
    id = db.Column(db.String(80), primary_key=True, default=generate_uuid)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    order_date = db.Column(db.DateTime, nullable=False, server_default=func.now())
    delivery_date = db.Column(db.DateTime)
    delivery_address = db.Column(db.String(300), nullable=False)
    delivered = db.Column(db.Boolean, nullable=False, default=False)
    total_price = db.Column(db.Numeric(5, 2))
    menu_item_id = db.Column(db.String(80), db.ForeignKey('menu_item.id'))
    customer_id = db.Column(db.String(80), db.ForeignKey('customer.id'))

    reviews = db.relationship('Review', backref="order")

    def __repr__(self):
        """String representation of model instance"""
        return f'<PlacedOrder {self.id}>'