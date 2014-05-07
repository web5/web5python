# -*- coding: utf-8 -*-

from flask import Flask
from webcore.configs import setting

def create_app():
    app = Flask(__name__)
    app.debug = setting.DEBUG
    app.config.db = setting.DB
    return app
