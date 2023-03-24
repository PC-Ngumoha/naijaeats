"""Definition of Review DB model"""
from app.extensions import db
from app.utilities import generate_uuid


class Review(db.Model):
    """Review DB model"""
    __tablename__ = 'review'
    id = db.Column(db.String(80), primary_key=True, default=generate_uuid)
    is_good = db.Column(db.Boolean, default=False)
    is_bad = db.Column(db.Boolean, default=True)
    comment = db.Column(db.Text, nullable=False)
    customer_id = db.Column(db.String(80), db.ForeignKey('customer.id'))
    order_id = db.Column(db.String(80), db.ForeignKey('placed_order.id'))

    def __repr__(self):
        """String representation of model instance"""
        return f'<Review {self.id}>'
