from flask_pymongo import PyMongo
# from flask_sqlalchemy import SQLAlchemy
import pymysql
# from flask import jsonify

# Mongo database connector
mongo = PyMongo()

## Define functions to connect to Google cloud MySQL

# Our instance connection name
db_connection_name = 'stock-project-294701:us-central1:stock-database'

## NOTE: must be running Cloud SQL Proxy on your local machine for this to work!
def open_connection():
    unix_socket = f'/cloudsql/{db_connection_name}'
    try:
        # if os.environ.get('GAE_ENV') == 'standard':
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='PApOEaPbJNOM62p1',
            db='stockdb',
            port=3306,
            cursorclass=pymysql.cursors.DictCursor
            
        )
        return conn
    except pymysql.MySQLError as e:
        print("EXCEPTION")
        print(e)


def get_companies(limit):
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute(f'SELECT * FROM CompanyInformation LIMIT {limit};')
        companies = cursor.fetchall()
        if result > 0:
            # got_c = jsonify(companies)
            got_c = companies   ## a list of dictionaries
        else:
            got_c = 'Nothing in DB'
    conn.close()
    return got_c


if __name__ == "__main__":
    print("Test db connection to MySQL")
    print(get_companies(limit=15))
