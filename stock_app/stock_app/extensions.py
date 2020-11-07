from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy

## Our database connectors
mongo = PyMongo()
sql_alchemy_db = SQLAlchemy()


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
    except pymysql.MySQLError as e:
        print(e)
    return conn


def get_companies():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM CompanyInformation;')
        companies = cursor.fetchall()
        if result > 0:
            got_c = jsonify(companies)
        else:
            got_c = 'Nothing in DB'
    conn.close()
    return got_c