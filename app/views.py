"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import base64

from werkzeug.utils import secure_filename

from app import app
from flask import render_template, request, redirect, url_for, flash
from .forms import PropertyForm, PROPERTY_TYPE
from app import db
from app.models import Listing
import psycopg2


###
# Routing for your application.
###

# connecting to database to read


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/properties', methods=['GET'])
def display_properties():
    properties = db.session.query(Listing).all()
    return render_template('properties.html', data=properties)


@app.route('/property/<propertyid>')
def getpropertyById(propertyid):
    propertyFromId = db.session.query(Listing).get(propertyid)
    return render_template('property.html', prop=propertyFromId)


@app.route('/property', methods=['GET', 'POST'])
def property_form():
    propertyForm = PropertyForm()

    if request.method == 'POST':
        if propertyForm.validate_on_submit():
            propertyTitle = propertyForm.propertyTitle.data
            location = propertyForm.location.data
            description = propertyForm.description.data
            roomsNumber = propertyForm.roomsNumber.data
            bathroomNumber = propertyForm.bathroomNumber.data
            price = propertyForm.price.data
            propertyType = dict(PROPERTY_TYPE).get(propertyForm.propertyType.data)
            photo = propertyForm.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename
            ))
            record = Listing(propertyTitle, location, description, roomsNumber, bathroomNumber, propertyType, price,
                             photo.filename)

            db.session.add(record)
            db.session.commit()

            flash('You have successfully filled out the form', 'success')
            return redirect(url_for('display_properties'))

        flash_errors(propertyForm)
    return render_template('property_form.html', form=propertyForm)



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
