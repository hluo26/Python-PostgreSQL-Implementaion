from app.city_weather import main
from app import db
from app.city_weather.models import City
from flask import render_template
import urllib.request
import json
import sys

api_key = '4d9cffc8109f4e2f9be310685d5ab9c6'

@main.route('/')
def display():
    cities = City.query.all()
    combination = load_data(cities)
    return render_template('home.html', combination = combination)


def load_data(cities):
    combination = []
    for x in cities:
        weather_info = {}
        zip1 = x.zip_code
        url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + str(zip1) + ',us&appid=' + api_key
        print(url, file=sys.stderr)
        html = urllib.request.urlopen(url)
        data = json.loads(html.read())
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        weather_info['Name'] = x.name
        weather_info['zip_code'] = x.zip_code
        weather_info['description'] = description
        weather_info['temperature'] = temperature
        weather_info['pressure'] = pressure
        weather_info['humidity'] = humidity
        weather_info['temp_max'] = temp_max
        weather_info['temp_min'] = temp_min
        combination.append(weather_info)
    return combination




