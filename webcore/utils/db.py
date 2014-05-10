# -*- coding: utf-8 -*-

from webcore.app import *
from flask.ext.sqlalchemy import SQLAlchemy

def init_db():
    db = SQLAlchemy(app)
    return db

db = init_db()
