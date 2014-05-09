# -*- coding: utf-8 -*-

import datetime
from flask.ext.security import UserMixin, RoleMixin
from webcore.utils.db import db
from flask.ext.security.utils import encrypt_password

class Role(db.model, RoleMixin):
    id = db.Column(db.Integer, primakry_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255) )

    def __init__(self, name, description):
        self.description = description
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model, UserMixin):
    time_now = datetime.now
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=time_now)
    roles = db.relationship('Role', backref=db.backref("user", lazy='joined'),
                            lazy='dynamic')
    last_login_time = db.Column(db.DateTime(), default=time_now, nullable=False)
    current_login_time = db.Column(db.DateTime(), default=time_now, nullable=False)
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer())
    username = db.Column(db.String(50), unique=True, nullable=False)
    remember_token = db.Column(db.String(255))
    authentication_token = db.Column(db.String(255))

    def __init__(self, name, email, password, active=True, username=None, roles=None):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.active = active
        self.roles = roles

    def __repr__(self):
        return '<User %r>' % self.username

    def clean(self, *args, **kwargs):
        if not self.username:
            self.username = User.generate_username(self.email)
        try:
            super(User, self).clean(*args, **kwargs)
        except:
            pass

    def set_password(self, password, save=False):
        self.password = encrypt_password(password)
        if save:
            self.save()
    @classmethod
    def generate_username(self, email):
        username = email.lower()
        for item in ['@', '.', '-', '+']:
            username.replace(item, '')
        return username

    @classmethod
    def display_name(self):
        return self.email or self.name


db.create_all()
admin = User('wenzhui', 'wenzhui@163.com', '123456')
db.session.add(admin)
db.session.commit()
users = User.query.all()
print users
print users[0].username

