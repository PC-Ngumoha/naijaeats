"""Contains the definition for the User model"""
from app.extensions import db
from app.models.menu_item import MenuItem
from app.models.review import Review
from app.utilities import generate_uuid
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """User model"""
    id = db.Column(db.String(50), primary_key=True, default=generate_uuid)
    first_name = db.Column(db.String(70), nullable=True)
    last_name = db.Column(db.String(70), nullable=True)
    org_name = db.Column(db.String(70), nullable=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_business = db.Column(db.Boolean(), nullable=False, default=False)
    address = db.Column(db.Text)
    city_id = db.Column(db.String(50), db.ForeignKey('city.id'),
                        nullable=False)
    menu = db.relationship('MenuItem', backref='restaurant', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)

    def __repr__(self) -> str:
        """String representation"""
        return f'<User {self.id} -> {self.email}>'
