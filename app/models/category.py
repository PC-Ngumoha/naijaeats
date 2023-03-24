"""Definition of Category DB model"""
from app.extensions import db
from app.models.menu_item import MenuItem
from app.utilities import generate_uuid


class Category(db.Model):
    """Category DB model"""
    __tablename__ = 'category'
    id = db.Column(db.String(80), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    menu = db.relationship('MenuItem', backref='category')

    def __repr__(self):
        """String representation of model instance"""
        return f'<Category {self.id} : {self.name}>'
