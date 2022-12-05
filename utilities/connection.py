from flask_mysqldb import MySQL


def connection(app):

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '1234'
    app.config['MYSQL_DB'] = 'ww-automation'

    mysql = MySQL(app)
    return mysql

