from backend import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(64), index=True, unique=True)
    planet_rotation = db.Column(db.Integer)
    planet_orbital_period = db.Column(db.Integer)
    planet_diameter = db.Column(db.Integer)
    planet_climate = db.Column(db.String(120), index=True, unique=True)
    planet_gravity = db.Column(db.String(120), index=True, unique=True)
    planet_surface_water = db.Column(db.Integer)
    planet_population = db.Column(db.Integer)

class Weather(db.Model):
    pass