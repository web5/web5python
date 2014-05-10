# -*- coding: utf-8 -*-

from webcore.utils.db import db
from webcore.app.accounts import user, role
db.drop_all()
db.create_all()

admin_role = dict(name='admin', description=u'超级管理员')
ar = role.add_role(admin_role)

admin = dict(name='wenzhui', email='wenzhui5@gmail.com', username='web5',
         password='123456', remember_token='xyz', authentication_token='abc',
         roles=[ar])

user.add_user(admin)

users = user.queryAll()
print users

