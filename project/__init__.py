from flask import Flask, render_template
from geopy.geocoders import Nominatim
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask import Flask



geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode("Chennai")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vips.db'
app.config['STATIC_URL_PATH'] = '/static'
app.secret_key='399c7904b286c80964a73685'
db= SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
from project import routes
