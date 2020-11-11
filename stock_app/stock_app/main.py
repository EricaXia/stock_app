from flask import Blueprint, render_template, Flask, request, make_response
from .extensions import mongo, open_connection, get_companies, get_prices
# import pprint

main = Blueprint('main', __name__)


@main.route('/')
def index():

    ## define MongoDB collection
    news_col = mongo.db.articles
    mdb_results = news_col.find().limit(15).sort("dt", -1)
    sql_results = get_companies(limit=15)  ## a list of dicts

    return render_template('index.html', mdb_results=mdb_results, sql_results=sql_results)


## Page template to show company stock info
@main.route('/<sym>')
def show(sym):
    price_results = get_prices(symbol=sym, limit='30')   ## a list of dicts
    return render_template('page.html', symbol=sym, price_results=price_results)


## Page not found
@main.errorhandler(404)
def not_found():
    return make_response(render_template("404.html"), 404)