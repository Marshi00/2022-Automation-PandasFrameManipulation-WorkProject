from flask import session
import utilities.configs as config

def download_limit(mysql,key,cursor):
    cursor.execute("SELECT limit_data.key,value,updated_at from limit_data where user_id = %s and limit_data.key = %s",(session['user_id'],key),)
    data = cursor.fetchone()

    if data:
        value_limit_download_template = int(data[1]) + 1
        if(value_limit_download_template <= config.LIMIT_TRY_DOWNLOAD):
            cursor.execute("UPDATE limit_data set value = %s where user_id = %s and limit_data.key = %s",(value_limit_download_template,session['user_id'],key),)
            mysql.connection.commit()
    else:
        value_limit_download_template = 1   
        cursor.execute("INSERT INTO limit_data(limit_data.user_id,limit_data.key,limit_data.value) values(%s,%s,%s)",(session['user_id'],key,value_limit_download_template,))        
        mysql.connection.commit()
    return value_limit_download_template