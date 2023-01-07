import requests
import os
from datetime import datetime

# class GetPlanetData():
#
#     def __init__(self, planet):
#         self.planet = planet
#         self.planet_name = 'unknown'
#         self.planet_rotation = 0
#         self.planet_orbital_period = 0
#         self.planet_diameter = 0
#         self.planet_climate = 'unknown'
#         self.planet_gravity = ''
#         self.planet_surface_water = ''
#         self.planet_population = 0
#
#     def fetch_raw_data_planet(self):
#         raw_data_planet = requests.get(f'https://swapi.dev/api/planets/{self.planet}/')
#         raw_data_planet.raise_for_status()
#         return raw_data_planet.json()
#
#     def fetch_planet_data(self):
#         data_planet = self.fetch_raw_data_planet()
#         self.planet_name = data_planet['name']
#         self.planet_rotation = data_planet['rotation_period']
#         self.planet_orbital_period = data_planet['orbital_period']
#         self.planet_diameter = data_planet['diameter']
#         self.planet_climate = data_planet['climate']
#         self.planet_gravity = data_planet['gravity']
#         self.planet_surface_water = data_planet['surface_water']
#         self.planet_population = data_planet['population']

class Request_Weather():
    pass

city = 'moscow'
date = '2022/04/07'
api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)

SECRET_KEY = os.environ.get('API_KEY')
print(SECRET_KEY)

raw_data = requests.get(api_url, headers={'X-Api-Key': SECRET_KEY})
raw_data.raise_for_status()
if raw_data.status_code == 200:
    data = raw_data.json()
    print(data)
else:
    print('Huston, we have a problem!')


