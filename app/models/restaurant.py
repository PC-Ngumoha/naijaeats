"""Definition of Restaurant DB model"""
from app.extensions import db
from app.models.menu_item import MenuItem
from app.utilities import generate_uuid
from sqlalchemy.sql import func


class Restaurant(db.Model):
    """Restaurant DB model"""
    __tablename__ = 'restaurant'
    id = db.Column(db.String(80), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100))
    website_url = db.Column(db.String(300))
    password = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=func.now())
    city_id = db.Column(db.String(80), db.ForeignKey('city.id'))
    menu = db.relationship('MenuItem', backref="restaurant")

    def __repr__(self):
        """String representation of model instance"""
        return f'<Restaurant {self.id} : {self.name}>'
