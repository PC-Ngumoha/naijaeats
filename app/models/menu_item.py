"""Contains the definition of the MenuItem model"""
from app.extensions import db
from app.utilities import generate_uuid


class MenuItem(db.Model):
    """MenuItem model"""
    id = db.Column(db.String(50), primary_key=True, default=generate_uuid)
    title = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.Text, nullable=False,
                          default='../static/images/naijafoods.jpeg')
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(precision=5, scale=2), nullable=False)
    category_id = db.Column(db.String(50), db.ForeignKey('category.id'),
                            nullable=False)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'),
                        nullable=True)

    def __repr__(self) -> str:
        """String representation"""
        return f'<MenuItem {self.id} -> {self.title}>'
