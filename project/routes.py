from project import app
from flask import render_template
from project.models import Item2

from project import location

@app.route('/')


@app.route('/home')
def hello_world():
    return render_template('home.html')
@app.route('/maps')
def map():
    markers = [
        {
            'lat': location.latitude,
            'lon': location.longitude,
            'popup': 'chennai'
        },
        {
          'lat':12.965965,
            'lon':80.125860,
            'popup':'stany home'
        },
        {
            'lat': 12.964696,
            'lon': 80.109803,
            'popup': 'my home'

        },
        {
            'lat':13.022554,
            'lon':80.167631,
            'popup':'rams home'
        }
    ]
    return render_template('map.html', markers=markers)


@app.route('/find vip')
def find_vip():
    items = Item2.query.all()
    # items = [
    # {'id': 1, 'name': 'parvesh', 'place': 'chennai'},
    # {'id': 2, 'name': 'sureshi', 'place': 'mumbai'},
    # {'id': 3, 'name': 'raaaa', 'place': 'delhi'}
    # ]
    return render_template('findvip.html', items=items)
