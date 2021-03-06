import requests
from datetime import datetime

class Credentials():
    def __init__(self, file):
        self.username = ''
        self.key = ''
        self.password = ''

    def get_username(self):
        pass

    def get_key(self):
        pass

    def get_password(self):
        pass

class Weather_request():
    def __init__(self, city, key, username):
        self.weather_key = key
        self.username = username
        self.city = city
        self.temperature = 0
        self.weather = ''
        self.id = 0
        self.weather_state_name = ''
        self.wind_degree = 0
        self.created = 0
        self.min_temp = 0
        self.max_temp = 0
        self.the_temp = 0
        self.timezone = 0
        self.wind = ''
        self.date_time = datetime.today()

    def request(self):
        self.raw_data = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.weather_key}&units=metric')
        return self.raw_data

    def get_data(self):
        if self.raw_data.status_code == 200:
            data = self.raw_data.json()
            self.temperature = data['main']['temp']
            self.weather = data['weather'][0]['description']
            self.id = data['id']
            self.weather_state_name = data['weather'][0]['main']
            self.wind_degree = data['wind']['deg']

            self.created = data['dt']
            #     applicable_date = data[0]['applicable_date']
            self.min_temp = data['main']['temp_min']
            self.max_temp = data['main']['temp_max']
            self.the_temp = data['main']['temp']
            self.timezone = data['timezone']
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

    def get_date_time(self):
        time = self.created + self.timezone
        return datetime.fromtimestamp(time)

    def get_weather(self):
        self.request()
        self.get_data()
        self.date_time = self.get_date_time()
        self.wind = self.convert_wind_from_degree_to_direction()


city = "London"
key = 12345
username = 12345
weather = Weather_request(city, key, username)
weather.get_weather()
print(city, weather.id, weather.weather_state_name, weather.wind_degree, weather.wind, weather.date_time,
      weather.max_temp, weather.max_temp, weather.the_temp)
print(weather.temperature, weather.weather)
