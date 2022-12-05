from curses.ascii import isdigit
import re
from flask import jsonify, request, session
from flask_bcrypt import Bcrypt


def register(app,mysql):
    if "email" in request.form and "password" in request.form  and "name" in request.form and "department" in request.form:

        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        department = request.form['department']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id,password from users where email = %s",(email,))
        user = cursor.fetchone()

        if user :
            return jsonify(
                error = True,
                msg = 'Email Already exists!'
            )
        else:
            cursor.execute("SELECT id from departments where id = %s",(department,))
            department_db = cursor.fetchone()
            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address!'
                return jsonify(
                    error = True,
                    msg = msg
                )
            elif len(name) < 3:
                msg = 'Name is Required and has to be at least 3 characters'
                return jsonify(
                    error = True,
                    msg = msg
                )
            elif not re.match(r'[A-Za-z0-9]+', name):
                msg = 'Name must contain only characters and numbers!'
                return jsonify(
                    error = True,
                    msg = msg
                )
            elif len(password) < 8:
                msg = 'Password is required and has to be at least 8 characters'
                return jsonify(
                    error = True,
                    msg = msg
                )
            elif department_db is None:
                msg = 'Department is not valid'
                return jsonify(
                    error = True,
                    msg = msg
                )
            else:
                bcrypt = Bcrypt(app)
                try:
                    cursor.execute('INSERT INTO users(email,password,name,department) VALUES (%s, %s, %s, %s)', (email, bcrypt.generate_password_hash(password), name,department))
                    user_registered = mysql.connection.commit()
                    msg = 'You have successfully registered!'
                    return jsonify(
                        error = False,
                        msg = msg
                    )
                except:
                    msg = 'Couldnt register your account, something went wrong!'
                    return jsonify(
                        error = True,
                        msg = msg
                    )
          
    else:
        return jsonify(
            error = True,
            msg = 'Something went wrong!'
        )
