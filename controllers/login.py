from flask import jsonify, request, session
from flask_bcrypt import Bcrypt


def login(app,mysql):
    if "email" in request.form and "password" in request.form :

        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id,password from users where email = %s",(email,))
        user = cursor.fetchone()

        bcrypt = Bcrypt(app)

        if user and bcrypt.check_password_hash(user[1], password):

            session.permanent = True
            session['user_id'] = user[0]

            return jsonify(
                error = False,
                msg = 'Successful login!'
            )
        else:
            return jsonify(
                error = True,
                msg = 'Email or password is wrong!'
            )
    else:
        return jsonify(
                error = True,
                msg = 'Something went wrong!'
            )
