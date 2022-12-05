
from datetime import datetime, timedelta
from flask import flash, send_file, session , redirect
import utilities.configs as config
import utilities.queries as query


def download_template(mysql):
    cursor = mysql.connection.cursor()

    value_limit_download_template = query.download_limit(mysql,'limit_download_template',cursor)
    
    cursor.execute("SELECT updated_at from limit_data where user_id = %s and limit_data.key = %s",(session['user_id'],'limit_download_template'),)
    check_date = cursor.fetchone()
    
    date_db = check_date[0]
    date_db += timedelta(minutes=config.LIMIT_MINUTES_DOWNLOAD)
    now = datetime.now() 

    if now > date_db:
        value_limit_download_template = 0
        cursor.execute("UPDATE limit_data set value = %s where user_id = %s and limit_data.key = %s",(value_limit_download_template,session['user_id'],'limit_download_template'),)
        mysql.connection.commit()

    if value_limit_download_template > config.LIMIT_TRY_DOWNLOAD:
        flash('You reached your limit you cant download more!')
        return redirect('/')
    else:
        return send_file("Standard_template - empty.xlsx", as_attachment=True)