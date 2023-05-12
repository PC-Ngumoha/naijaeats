"""Contains the definition of the Review model"""
from app.extensions import db
from app.utilities import generate_uuid


class Review(db.Model):
    """Review model"""
    id = db.Column(db.String(), primary_key=True, default=generate_uuid)
    is_good = db.Column(db.Boolean, nullable=False, default=False)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'),
                        nullable=False)
    placed_order_id = db.Column(db.String(50),
                                db.ForeignKey('placed_order.id'),
                                nullable=False)

    def __repr__(self) -> str:
        """String representation"""
        return f'<Review {self.id}>'
