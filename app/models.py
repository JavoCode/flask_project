from numpy.core import unicode

from . import db
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    property_title = db.Column(db.String(80))
    location = db.Column(db.String(80))
    rooms_number = db.Column(db.String(80))
    bathroom_number = db.Column(db.String(80))
    property_type = db.Column(db.String(80))
    price = db.Column(db.String(80))
    description = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    username = db.Column(db.String(80), unique=True)

    def __init__(self, propertyTitle, location, description, roomsNumber, bathroomNumber, propertyType, price, photo):
        self.property_title = propertyTitle
        self.location = location
        self.description = description
        self.rooms_number = roomsNumber
        self.bathroom_number = bathroomNumber
        self.property_type = propertyType
        self.price = price
        self.photo = photo

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

