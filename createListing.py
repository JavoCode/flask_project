from app import db
from app.models import Listing

listing = Listing(propertyTitle="West City", location="10 Kingston. Linstone Crescent", roomsNumber="5", bathroomNumber="2",
                   propertyType="House", price="15000", description="Very large house", photo="none")
db.session.add(listing)
db.session.commit
