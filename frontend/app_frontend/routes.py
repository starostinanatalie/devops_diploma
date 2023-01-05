from flask import render_template, flash, redirect, url_for
from app_frontend import app_frontend

@app_frontend.route('/')
@app_frontend.route('/index')
def index():
    planet_name = {'name': ['Tatooine', 'Alderaan', 'Coruscant']}
    planets = [{'name': 'Tatooine', 'size': 'middle planet', 'terrain': 'desert'}]

    return render_template('index.html', planets=planets)
