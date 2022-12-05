from datetime import timedelta
from textwrap import wrap
from flask import Flask
from flask_wtf.csrf import CSRFProtect
import utilities.connection as db_conn
import utilities.utilities as utility
import utilities.decorator as decorator
import controllers.index as index_controller
import controllers.login as login_controller
import controllers.logout as logout_controller
import controllers.register as register_controller
import controllers.download_template as download_template_controller
import controllers.download_result as download_result_controller
import controllers.upload_template as upload_template_controller

app = Flask(__name__)

# app.register_blueprint(index_blueprint)

csrf = CSRFProtect(app)

app.secret_key = 'some_random_secret_key_that_you_wont_be_able_to_guess?_xd'
app.permanent_session_lifetime	= timedelta(days=1)

mysql = db_conn.connection(app)

LIMIT_MINUTES_DOWNLOAD = 30

@app.route('/')
def home():
    return index_controller.index(mysql)

@app.route('/login',methods=["POST"])
@decorator.not_logged_required
def login():
    return login_controller.login(app,mysql)

@app.route('/register',methods=["POST"])
@decorator.not_logged_required
def register():
    return register_controller.register(app,mysql)

@app.route('/logout',methods=["POST",'GET'])
@decorator.login_required
def logout():
    return logout_controller.logout()

@app.route('/download_template')
@decorator.login_required
def download_template():
    return download_template_controller.download_template(mysql)

@app.route('/download_result/<result>')
@decorator.login_required
def download_result(result):
    return download_result_controller.download_result(mysql,result)

@app.route('/upload_template',methods=["POST","GET"])
@decorator.login_required
def upload_template():
    return upload_template_controller.upload_template(mysql)

if __name__ == "__main__":
    app.run(debug=True)
