from flask import Blueprint, render_template, Flask, request, make_response, redirect, url_for
from pymysql import ProgrammingError
from .extensions import mongo, open_connection, get_companies, get_prices
from .forms import SymSearchForm

main = Blueprint('main', __name__)


@main.route('/', methods=['GET','POST'])
def index():

    ## define MongoDB collection
    news_col = mongo.db.articles
    mdb_results = news_col.find().limit(15).sort("dt", -1)
    sql_results = get_companies(limit=15)  ## a list of dicts

    ## Search feature
    form = SymSearchForm(request.form)
    if request.method == 'POST':
        sym_query = form.symbol.data
        return redirect(url_for('.show', sym=sym_query))

    return render_template('index.html', mdb_results=mdb_results, sql_results=sql_results, form=form)


## Page template to show company stock info
@main.route('/<sym>', methods=['GET'])
def show(sym):
    price_results = get_prices(symbol=sym, limit='30')   ## a list of dicts
    return render_template('page.html', symbol=sym, price_results=price_results)


## Page not found
@main.errorhandler(404)
def not_found():
    return make_response(render_template("404.html"), 404)


## If stock taable is not found, return error page
@main.errorhandler(ProgrammingError)
def handle_error(e):
    return '<h1>Table not found!</h1>', 400