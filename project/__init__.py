from flask import Flask, render_template
from geopy.geocoders import Nominatim
from flask_sqlalchemy import SQLAlchemy




geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode("Chennai")



#print("The latitude of the location is: ", location.latitude)
#print("The longitude of the location is: ", location.longitude)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vips.db'
app.secret_key='399c7904b286c80964a73685'
db= SQLAlchemy(app)
from project import routes
#
# class Item2(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(length=30), nullable=False, unique=True)
#     latitude = db.Column(db.Integer(), nullable=False)
#     longitude = db.Column(db.Integer(), nullable=False)
#     #barcode = db.Column(db.String(length=12), nullable=False, unique=True)
#     place = db.Column(db.String(length=1024), nullable=False,)
#
#     def __repr__(self):
#         return f'Item2 {self.name}'



#
# @app.route('/')
#
#
# @app.route('/home')
# def hello_world():
#     return render_template('home.html')
# @app.route('/maps')
# def map():
#     markers = [
#         {
#             'lat': location.latitude,
#             'lon': location.longitude,
#             'popup': 'chennai'
#         },
#         {
#           'lat':12.965965,
#             'lon':80.125860,
#             'popup':'stany home'
#         },
#         {
#             'lat': 12.964696,
#             'lon': 80.109803,
#             'popup': 'my home'
#
#         },
#         {
#             'lat':13.022554,
#             'lon':80.167631,
#             'popup':'rams home'
#         }
#     ]
#     return render_template('map.html', markers=markers)
#
#
# @app.route('/find vip')
# def find_vip():
#     items = Item2.query.all()
#     # items = [
#     # {'id': 1, 'name': 'parvesh', 'place': 'chennai'},
#     # {'id': 2, 'name': 'sureshi', 'place': 'mumbai'},
#     # {'id': 3, 'name': 'raaaa', 'place': 'delhi'}
#     # ]
#     return render_template('findvip.html',items=items)
#
#
#
#
