from flask import session , jsonify

def logout():
    session.pop('user_id',None)
    return jsonify(
                error = False,
                msg = 'Logged out'
            )