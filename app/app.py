import os
import datetime

from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template, Blueprint
from json import loads

from flask_sqlalchemy import SQLAlchemy
import logging


APP_DIR = os.path.dirname(os.path.abspath(__file__))
print(APP_DIR, " current dir\n\n")
STATIC_FOLDER = os.path.join(APP_DIR, 'react_folder/build/static')
print(STATIC_FOLDER)
TEMPLATE_FOLDER = os.path.join(APP_DIR, 'react_folder/build/')


# app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app = Flask(__name__, static_folder="../react_folder/build/static",
            template_folder='../react_folder/build/')

'''
DO
NOT
LEAVE
IN
PRODUCTION
'''


# host = os.environ['host']
# db = os.environ['db']
# user = os.environ['user']
# port = os.environ['port']
# pwd = os.environ['pwd']
#
# query = 'postgresql://{user}:{pwd}@{host}:{port}/{db}'.format(user=user, pwd=pwd, host=host, port=port, db=db)

app.config['SQLALCHEMY_DATABASE_URI'] = query

odb = SQLAlchemy(app)

# app.secret_key = os.environ['APP_SECRET_KEY']
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
# app.config['JWT_COOKIE_SECURE'] = True
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
# app.config['JWT_COOKIE_CSRF_PROTECT'] = True

app.config['JWT_SECRET_KEY'] = 'SUPER-HOT'


class User(odb.Model):
    id = odb.Column(odb.Integer, primary_key=True)
    name = odb.Column(odb.String(80))
    email = odb.Column(odb.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login_page():
    return "it's working"


if __name__ == '__main__':
    app.run()
