from flask import render_template, flash, redirect, url_for
from app_frontend import app_frontend

@app_frontend.route('/')
@app_frontend.route('/index')
def index():
    planet = {'name': ['Tatooine', 'Alderaan', 'Coruscant'],
              'terrain': ['desert', 'grasslands and mountains', 'cityscape'],
              'type': ['big planet', 'middle planet', 'small planet']}

    return render_template('index.html', planet = planet)