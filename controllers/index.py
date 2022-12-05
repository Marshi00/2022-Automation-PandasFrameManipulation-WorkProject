from datetime import datetime, timedelta
import utilities.connection as db_conn
import utilities.configs as config
from flask import Blueprint, render_template, session


def index(mysql):
    cursor = mysql.connection.cursor()
    departments = None

    if "user_id" in session:
        cursor.execute(
            "SELECT limit_data.key,limit_data.value,updated_at from limit_data where user_id = %s and limit_data.key = %s",
            (session['user_id'], 'limit_download_template'), )
        data = cursor.fetchone()
        if data:
            value_limit_download_template = data[1]
        else:
            value_limit_download_template = 0

        check_date = datetime(1970, 1, 1) if data is None else data[2]
        check_date += timedelta(minutes=config.LIMIT_MINUTES_DOWNLOAD)

        now = datetime.now()
        value_limit_download_template = int(
            value_limit_download_template) < config.LIMIT_TRY_DOWNLOAD or now > check_date
    else:
        value_limit_download_template = None
        cursor.execute("SELECT id,department from departments")
        departments = cursor.fetchall()

    return render_template("index.html", value_limit_download_template=value_limit_download_template,
                           departments=departments)
