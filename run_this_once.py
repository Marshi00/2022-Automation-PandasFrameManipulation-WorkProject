import utilities.connection;
from flask import Flask

from flask_mysqldb import MySQL,MySQLdb

#conn = utilities.connection.connection()
app = Flask(__name__)

app.secret_key = 'some_random_secret_key_that_you_wont_be_able_to_guess?_xd'
conn = utilities.connection.connection(app)

# CREATE TABLE `arshian_python_project`.`limit_data` ( `id` INT NOT NULL AUTO_INCREMENT , `user_id` INT NOT NULL , `key` VARCHAR(50) NOT NULL , `value` VARCHAR(50) NOT NULL , `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (`id`)) ENGINE = InnoDB; app.config['MYSQL_HOST'] = 'localhost'
# ALTER TABLE `limit_data` ADD FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE; 
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'sasha093021422143'
#app.config['MYSQL_DB'] = 'ww-automation'

#conn = MySQL(app)

#Creating a connection cursor
cursor = conn.connection.cursor(MySQLdb.cursors.DictCursor)
 
# #Executing SQL Statements
# cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
# cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
# cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
# #Saving the Actions performed on the DB
# conn.connection.commit()
 
# #Closing the cursor
# cursor.close()