#app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_type):

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type+'.py')
    app.config.from_pyfile(configuration)

    db.init_app(app)
    bootstrap.init_app(app)


    from app.city_weather import main

    app.register_blueprint(main)

    return app