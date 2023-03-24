"""Definition of City database model"""
from app.extensions import db
from app.models.customer import Customer
from app.models.restaurant import Restaurant
from app.utilities import generate_uuid

class City(db.Model):
    """City database model"""
    __tablename__ = 'city'
    id = db.Column(db.String(80), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(20))
    customers = db.relationship('Customer', backref='city')
    restaurants = db.relationship('Restaurant', backref='city')


    def __repr__(self):
        """String representation of model instance"""
        return f'<City {self.id} : {self.name}>'
