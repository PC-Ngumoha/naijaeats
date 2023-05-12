"""Contains the definition of the 'City' model"""
from app.extensions import db
from app.models.user import User
from app.utilities import generate_uuid


class City(db.Model):
    """City model"""
    id = db.Column(db.String(50), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(30), nullable=False, unique=True)
    zip_code = db.Column(db.String(20))
    users = db.relationship('User', backref='city', lazy=True)

    def __repr__(self) -> str:
        """String representation of this object"""
        return f'<City {self.id} -> {self.name}>'
