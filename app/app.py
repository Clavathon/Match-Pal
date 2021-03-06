import os
import datetime

from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template, Blueprint
from json import loads
from flask_sqlalchemy import SQLAlchemy
from database import db_session
from models import *

import logging


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

query = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = query

odb = SQLAlchemy(app)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = True
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
# app.config['JWT_SECRET_KEY'] = 'SUPER-HOT'


# class User(odb.Model):
#     id = odb.Column(odb.Integer, primary_key=True)
#     name = odb.Column(odb.String(80))
#     email = odb.Column(odb.String(120), unique=True)
#
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def __repr__(self):
#         return '<Name %r>' % self.name


# print(odb)

# odb.create_all()


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login_page():
    return "it's working"


# @app.route('/user/<user>', methods=['GET'])
# def user_creation(user):
#     new_user = User(user, user+"@blasphemy.com")
#     try:
#         odb.session.add(new_user)
#         print(new_user)
#         odb.session.commit()
#         print("\n\n\nyeah, we got fresh meat\n\n\n")
#     except Exception as e:
#         odb.session.rollback()
#         print("\n\n\n\n\nDone goof\n\n\n\n\n")
#         raise e
#     finally:
#         odb.session.close()
#
#     return "it's working"

@app.route('/user/<user>', methods=['GET'])
def user_creation(user):
    new_user = User(user, user+"@blasphemy.com")
    try:
        dbs_session.add(new_user)
        print(new_user)
        dbs_session.commit()
        print("\n\n\nyeah, we got fresh meat\n\n\n")
    except Exception as e:
        dbs_session.rollback()
        print("\n\n\n\n\nDone goof\n\n\n\n\n")
        raise e
    finally:
        dbs_session.close()

    return "it's working"


if __name__ == '__main__':
    app.run()
