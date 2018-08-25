import os
import datetime

from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template, Blueprint
from json import loads
import logging


app = Flask(__name__)

# app.secret_key = os.environ['APP_SECRET_KEY']
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
# app.config['JWT_COOKIE_SECURE'] = True
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
# app.config['JWT_COOKIE_CSRF_PROTECT'] = True

app.config['JWT_SECRET_KEY'] = 'SUPER-HOT'


@app.route('/login', methods=['GET'])
def login_page():

    return "it's working"


if __name__ == '__main__':
    app.run(host='localhost', load_dotenv='.env')
