import requests
from datetime import datetime

planet = 3

raw_data_planet = requests.get(f'https://swapi.dev/api/planets/{planet}/')
if raw_data_planet.status_code == 200:
    data_planet = raw_data_planet.json()
    planet_name = data_planet['name']
    print(planet_name)
else:
    print('Huston, we have a problem')

