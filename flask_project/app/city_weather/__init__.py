#city_weather/__init__.py

from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')

from app.city_weather import routes


