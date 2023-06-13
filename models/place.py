from models.base_model import BaseModel
from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from models import storage
from os import getenv
from models.base_model import Base

class Place(BaseModel):
    """This class defines a place by various attributes"""
    __tablename__ = 'places'

    # existing code

    if getenv("HBNB_TYPE_STORAGE") == "db":
        metadata = Base.metadata
        place_amenity = Table('place_amenity', metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     primary_key=True, nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True, nullable=False))
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 backref="places",
                                 viewonly=False)
    else:
        @property
        def amenities(self):
            """getter attribute amenities that returns the list of
            Amenity instances based on the attribute amenity_ids
            """
            amenity_objs = []
            amenities = storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.id in self.amenity_ids:
                    amenity_objs.append(amenity)
            return amenity_objs

        @amenities.setter
        def amenities(self, obj):
            """setter attribute amenities that handles append method
            for adding an Amenity.id to the attribute amenity_ids
            """
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
