import os
from flask import Flask
from sqlalchemy import URL
from flask_sqlalchemy import SQLAlchemy

TEMPLATES_DIR = os.path.dirname(os.path.abspath(__file__)) + '/views/templates'

STATIC_DIR = os.path.dirname(os.path.abspath(__file__)) + '/views/static'

APP = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

# Preencha aqui com os dados do seu banco de dados MySQL.
# Alguns campos estão com os dados padrões, altere caso necessário.
# No caso de dúvidas, leia o README
URL_OBJECT = URL.create(
    'mysql+pymysql',
    username='root',
    password='',
    host='localhost',
    port=3306,
    database='estoque'
)

APP.config['SQLALCHEMY_DATABASE_URI'] = URL_OBJECT

DB = SQLAlchemy(APP)

SECRET_KEY = os.urandom(10)

APP.config['SECRET_KEY'] = SECRET_KEY
