import requests
from datetime import datetime

class Get

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

city = 'Moscow'
date = '2022/04/07'

city_request = requests.get(f'https://www.metaweather.com/api/location/search/?query={city}')
if city_request.status_code == 200:
    city_data = city_request.json()
    city_id = city_data[0]['woeid']
else:
    print("Huston, we have a problem")

raw_data = requests.get(f'https://www.metaweather.com/api/location/{city_id}/{date}')
raw_data.raise_for_status()
if raw_data.status_code == 200:
    data = raw_data.json()
    id = data[0]['id']
    weather_state_name = data[0]['weather_state_name']
    wind_direction_compass = data[0]['wind_direction_compass']
    created = data[0]['created']
    applicable_date = data[0]['applicable_date']
    min_temp = data[0]['min_temp']
    max_temp = data[0]['max_temp']
    the_temp = data[0]['the_temp']
    print(id, weather_state_name, wind_direction_compass, created, applicable_date, max_temp, max_temp, the_temp)
else:
    print('Huston, we have a problem!')