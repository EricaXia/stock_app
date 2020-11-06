from flask import Blueprint, render_template
from flask_bootstrap import Bootstrap
from .extensions import mongo
import pprint

main = Blueprint('main', __name__)


@main.route('/')
def index():

    ## Return Mongodb results
    news_col = mongo.db.articles
    # res = news_col.find_one()
    results = news_col.find().limit(10)
    return render_template('index.html', results=results)