import os
import datetime

from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template, Blueprint
from json import loads
import logging


APP_DIR = os.path.dirname(os.path.abspath(__file__))
print(APP_DIR, " current dir\n\n")
STATIC_FOLDER = os.path.join(APP_DIR, 'react_folder/build/static')
print(STATIC_FOLDER)
TEMPLATE_FOLDER = os.path.join(APP_DIR, 'react_folder/build/')


# app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app = Flask(__name__, static_folder="../react_folder/build/static",
            template_folder='../react_folder/build/')


# app.secret_key = os.environ['APP_SECRET_KEY']
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
# app.config['JWT_COOKIE_SECURE'] = True
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
# app.config['JWT_COOKIE_CSRF_PROTECT'] = True

app.config['JWT_SECRET_KEY'] = 'SUPER-HOT'


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login_page():
    return "it's working"


if __name__ == '__main__':
    app.run(host='localhost', load_dotenv='.env')
