from flask import Flask 
from .extensions import mongo, sql_alchemy_db
from .main import main


def create_app(config_object='stock_app.settings'):
    ## initialize Flask app
    app = Flask(__name__)
    ## load config file
    app.config.from_object(config_object)
    ## bind the db handlers to the app
    mongo.init_app(app)
    sql_alchemy_db.init_app(app)

    app.register_blueprint(main)
    return app