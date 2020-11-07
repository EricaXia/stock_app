from flask import Blueprint, render_template, Flask, request, make_response, jsonify
from .extensions import mongo, sql_alchemy_db
# import pprint

main = Blueprint('main', __name__)

# company_info = sql_alchemy_db.Table('CompanyInformation', sql_alchemy_db.metadata, autoload=True, autoload_with=sql_alchemy_db.engine)



@main.route('/')
def index():

    ## define MongoDB collection
    news_col = mongo.db.articles
    mdb_results = news_col.find().limit(15).sort("dt", -1)
    # sql_results = sql_alchemy_db.session.query(company_info).all()

    return render_template('index.html', mdb_results=mdb_results)