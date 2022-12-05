from datetime import datetime, timedelta
from flask import  send_file, session ,redirect
import utilities.configs as config
import utilities.queries as query

def download_result(mysql,result):
    # check if the file belongs to the user.
    if result.split('_')[0] == str(session['user_id']):
        cursor = mysql.connection.cursor()

        value_limit_download_result = query.download_limit(mysql,'limit_download_result',cursor)

        cursor.execute("SELECT updated_at from limit_data where user_id = %s and limit_data.key = %s",(session['user_id'],'limit_download_result'),)
        check_date = cursor.fetchone()

        date_db = check_date[0]
        date_db += timedelta(minutes=config.LIMIT_MINUTES_DOWNLOAD)
        now = datetime.now() 

        if now > date_db:
            value_limit_download_result = 0
            cursor.execute("UPDATE limit_data set value = %s where user_id = %s and limit_data.key = %s",(value_limit_download_result,session['user_id'],'limit_download_result'),)
            mysql.connection.commit()

        if value_limit_download_result > config.LIMIT_TRY_DOWNLOAD:
            print(value_limit_download_result)
            return redirect('/')
        else:
            return send_file('files/'+result+'.zip', as_attachment=True)
            # how to pass parameters in redirect ?
    else:
        return redirect('/')