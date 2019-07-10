#!/usr/bin/python
#coding: utf-8

from flask import Flask, render_template, request
from flask_autoindex import AutoIndex
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['pdf', 'zip', 'iso'])

app = Flask(__name__)
AutoIndex(app, browse_root="D:/Stockage/Flask/Download")
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload')
def upload():  
    return render_template("upload.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(("D:/Stockage/Flask/Upload/"+filename), app.config['MAX_CONTENT_LENGTH'])  
            return render_template("success.html", name = file.filename) 
        else:
             return render_template("fail.html")
	

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
