#!/usr/bin/python
#coding: utf-8

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_autoindex import AutoIndex
from werkzeug.utils import secure_filename
import os


application = Flask(__name__)
socketio = SocketIO(application)
application.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024 #(25 Mo)
ALLOWED_EXTENSIONS = set(['pdf', 'zip', '7z', 'tar', 'tar.gz', 'rar', 'py'])


@application.route('/')
def index():  
    return render_template('index.html')  


@application.route('/chat')
def chat():
    return render_template('chat.html')

@socketio.on('connected')
def conn(msg):
        return {'data':'Ok'}

@socketio.on('client_message')
def receive_message(data):
        emit('server_message', data, broadcast=True)


share = AutoIndex(application, os.path.curdir+'/download', add_url_rules=False)
@application.route('/download/')
@application.route('/download/<path:path>')
def autoindex(path='.'):
    return share.render_autoindex(path)


@application.route('/upload')
def upload():  
    return render_template('upload.html')  

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@application.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(('upload/'+filename), application.config['MAX_CONTENT_LENGTH'])  
            return render_template("success.html", name = file.filename) 
        else:
             return render_template("fail.html")
	

if __name__ == "__main__":
    socketio.run(application, host='0.0.0.0', port=80)
