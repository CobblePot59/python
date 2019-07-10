#!/usr/bin/python
#coding: utf-8

from flask import Flask
from flask_autoindex import AutoIndex


app = Flask(__name__)
AutoIndex(app, browse_root="D:/Stockage/Flask/")

if __name__ == '__main__':
	app.run(host='', port=8080)
