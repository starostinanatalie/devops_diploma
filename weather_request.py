import requests
from datetime import datetime

weather_key = '0622e80182c6090dc5a26b80c419177f'
username = 'starnatalie'
city = 'Moscow'

raw_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric')
print(raw_data)

if raw_data.status_code == 200:
    data = raw_data.json()
    print(data)
    temperature = data['main']['temp']
    weather = data['weather'][0]['description']
    print(temperature, weather)
else:
    print('Huston, we have a problem!')