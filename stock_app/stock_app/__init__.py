from flask import Flask 
from flask_bootstrap import Bootstrap
from .extensions import mongo
from .main import main

def create_app(config_object='stock_app.settings'):
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(config_object)
    mongo.init_app(app)
    app.register_blueprint(main)
    return app