"""Definition of Customer DB model"""
from app.extensions import db
from app.models.review import Review
from app.models.placed_order import PlacedOrder
from app.utilities import generate_uuid
from sqlalchemy.sql import func


class Customer(db.Model):
    """Customer DB model"""
    __tablename__ = 'customer'
    id = db.Column(db.String(80), primary_key=True, default=generate_uuid)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    phone_no = db.Column(db.String(20))
    password = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=func.now())
    city_id = db.Column(db.String(80), db.ForeignKey('city.id'))

    reviews = db.relationship('Review', backref="customer")
    orders = db.relationship('PlacedOrder', backref="customer")

    def __repr__(self):
        """String representation of model instance"""
        return f'<Customer {self.id} : {self.firstname}>'
