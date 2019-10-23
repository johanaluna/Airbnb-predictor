from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import urllib.request
import json
import pickle as p


"""create and configures an instance of a flask app"""
APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)


@APP.route('/')
def root():
    message = 'welcome home'
    return render_template('base.html', message=message)

@APP.route('/request')
def request_data():
    return "Requesting data"

@APP.route('/predictor')
def predictor():
    prediction= 3
    return render_template('predictor.html', parameter = prediction)

# Here lies the dummy data.
@APP.route('/dummy')
def dummy_data():
    with open('dummy.json', 'r') as f:
        dummy = json.load(f)
    return dummy

@APP.route('/topredict')
def request_info():
    url = "http://127.0.0.1:5000/dummy"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data

# Above lies the dummy data.

if __name__ == '__main__':
    APP.run(debug=True)
