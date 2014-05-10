# -*- coding: utf-8 -*-

from flask import Flask
from webcore.configs import setting

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = setting.DB
    app.debug = setting.DEBUG
    return app

app = create_app()
