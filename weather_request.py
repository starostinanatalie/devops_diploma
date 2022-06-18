import requests
from datetime import datetime

class Weather_request():
    def __init__(self, city):
        self.weather_key = '0622e80182c6090dc5a26b80c419177f'
        self.username = 'starnatalie'
        self.city = city

    def request(self):
        self.raw_data = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric')
        return self.raw_data

    def get_data(self):
        if self.raw_data.status_code == 200:
            self.data = self.raw_data.json()
            self.temperature = self.data['main']['temp']
            self.weather = self.data['weather'][0]['description']
            self.id = self.data['id']
            self.weather_state_name = self.data['weather'][0]['main']
            self.wind_degree = self.data['wind']['deg']

            self.created = self.data['dt']
            #     applicable_date = data[0]['applicable_date']
            self.min_temp = self.data['main']['temp_min']
            self.max_temp = self.data['main']['temp_max']
            self.the_temp = self.data['main']['temp']
        else:
            print('Huston, we have a problem!')

    def convert_wind_from_degree_to_direction(self):
        if 11.25 < self.wind_degree < 33.75:
            return 'NNE'
        elif 33.75 < self.wind_degree < 56.25:
            return 'NE'
        elif 56.25 < self.wind_degree < 78.75:
            return 'ENE'
        elif 78.75 < self.wind_degree < 101.25:
            return 'E'
        elif 101.25 < self.wind_degree < 123.75:
            return 'ESE'
        elif 123.75 < self.wind_degree < 146.25:
            return 'SE'
        elif 146.25 < self.wind_degree < 168.75:
            return 'SSE'
        elif 168.75 < self.wind_degree < 191.25:
            return 'S'
        elif 191.25 < self.wind_degree < 213.75:
            return 'SSW'
        elif 213.75 < self.wind_degree < 236.25:
            return 'SW'
        elif 236.25 < self.wind_degree < 258.75:
            return 'WSW'
        elif 258.75 < self.wind_degree < 281.25:
            return 'W'
        elif 281.25 < self.wind_degree < 303.75:
            return 'WNW'
        elif 303.75 < self.wind_degree < 326.25:
            return 'NW'
        elif 326.25 < self.wind_degree < 348.75:
            return 'NNW'
        else:
            return 'N'

city = "Moscow"
weather = Weather_request(city)
print(weather.data)
wind_direction_compass = weather.convert_wind_from_degree_to_direction()
print(id, weather.weather_state_name, weather.wind_degree, weather.wind_direction_compass, weather.created,
      weather.max_temp, weather.max_temp, weather.the_temp)
print(weather.temperature, weather.weather)
