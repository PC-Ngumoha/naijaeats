"""Contains the definition of the PlacedOrder model"""
from app.extensions import db
from app.models.menu_item import MenuItem
from app.models.review import Review
from app.utilities import generate_uuid
from datetime import datetime

# Creating an association table for the many-to-many relationship
# between the placed_order and the menu_item.
order_menuitem = db.Table('order_menuitem',
                          db.Column('menu_item_id',
                                    db.String(50),
                                    db.ForeignKey('menu_item.id'),
                                    primary_key=True),
                          db.Column('placed_order_id',
                                    db.String(50),
                                    db.ForeignKey('placed_order.id'),
                                    primary_key=True)
                          )


class PlacedOrder(db.Model):
    """PlacedOrder model"""
    id = db.Column(db.String(50), primary_key=True, default=generate_uuid)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    delivery_date = db.Column(db.DateTime)
    delivery_address = db.Column(db.Text, nullable=False)
    total_price = db.Column(db.Float)
    delivered = db.Column(db.Boolean, default=False)
    reviews = db.relationship('Review', backref='order', lazy=True)
    menu = db.relationship('MenuItem', secondary=order_menuitem,
                           backref='orders')

    def __repr__(self) -> str:
        """String representation"""
        return f'<Order {self.id}>'
