from flask import Flask,request, render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://haoluo:0826@localhost/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning


db = SQLAlchemy(app)


class City(db.Model):

    __tablename__ = 'City'
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(50))

    def __init__(self, name, zip_code):
        self.name = name
        self.zip_code = zip_code

    def __repr__(self):
        return 'The Name is {}, and the zip code is {}'.format(self.name, self.zip_code)


class Weather(db.Model):

    __tablename__ = 'Weather'
    wid = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    temperature = db.Column(db.Float)
    pressure = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    temp_min = db.Column(db.Float)
    temp_max = db.Column(db.Float)

    city_name = db.Column(db.String(100), db.ForeignKey('City.name'), nullable=False)

    def __init__(self, description, temperature, pressure, humidity, temp_min, temp_max, city_name):
        self.description = description
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.city_name = city_name

    def __repr__(self):
        return '{} degree, {}'.format(self.temperature, self.description)


@app.route('/')
def start():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
