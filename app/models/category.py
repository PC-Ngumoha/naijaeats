"""Contains the definition of the Category class"""
from app.extensions import db
from app.models.menu_item import MenuItem
from app.utilities import generate_uuid


class Category(db.Model):
    """Category model"""
    id = db.Column(db.String(50), primary_key=True, default=generate_uuid)
    title = db.Column(db.String(30), nullable=False, unique=True)
    menu = db.relationship('MenuItem', backref='category', lazy=True)

    def __repr__(self) -> str:
        """String representation"""
        return f'<Category {self.id} -> {self.title}>'
