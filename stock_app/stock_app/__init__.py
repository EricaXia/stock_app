from flask import Flask 
from flask_bootstrap import Bootstrap
from .extensions import mongo, sql_alchemy
from .main import main


def create_app(config_object='stock_app.settings'):
    ## initialize Flask app
    app = Flask(__name__)
    
    ## make Bootstrap templates
    Bootstrap(app)
    app.config.from_object(config_object)

    ## bind the db handlers to the app
    mongo.init_app(app)
    sql_alchemy.init_app(app)

    app.register_blueprint(main)
    return app