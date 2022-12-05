import shutil
import time
from flask import  jsonify, session , request
import utilities.utilities as utility
import pathtest

def upload_template(mysql):
     # check if the post request has the file part
    if 'file' not in request.files:
        return jsonify(
            error = True,
            msg = 'No file selected1'
        )
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
            return jsonify(
            error = True,
            msg = 'No file selected2'
        )
    if file and utility.allowed_file(file.filename):

        # filename = secure_filename(file.filename)
        path = pathtest.operate_on_xlsx(file)
        zipFilename = str(session['user_id']) + "_" + str(int(time.time()))
        # zip the operations folder
        shutil.make_archive(str('files/'+zipFilename), 'zip', path)
        # delete operation folder after it got ziped
        shutil.rmtree(path, ignore_errors=False, onerror=None)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE limit_data set value = %s where user_id = %s and limit_data.key = %s",(0,session['user_id'],'limit_download_result'),)
        mysql.connection.commit()
        
        return jsonify(
            error = False,
            file_name = zipFilename,
            msg = 'Operation successful'
        )
    else :
        return jsonify(
            error = True,
            msg = 'File has to be type Xlsx'
        )