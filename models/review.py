from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel):
    """This class defines a review by various attributes"""
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    reviews = relationship("Review", cascade="all, delete-orphan", backref="user")
