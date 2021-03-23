from flask_wtf import FlaskForm, validators
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import IntegerField, TextAreaField, SelectField, StringField
from wtforms.validators import DataRequired

PROPERTY_TYPE = [('1', 'House'), ('2', 'Apartment'), ('3', 'Town House'), ('4', 'Loft')]


class PropertyForm(FlaskForm):
    propertyTitle = StringField('Property Title', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    roomsNumber = IntegerField('No of Rooms', validators=[DataRequired()])
    bathroomNumber = IntegerField('No of Bathrooms', validators=[DataRequired()])
    propertyType = SelectField('Property Type', validators=[DataRequired()], choices=PROPERTY_TYPE)
    price = IntegerField('Price', validators=[DataRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])


class PhotoForm(FlaskForm):
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
    description = StringField('Description', validators=[DataRequired()])
