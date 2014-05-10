# -*- coding: utf-8 -*-

from webcore.utils.db import db
from webcore.modules.accounts.models import User

'''
    @user {}

'''
def add_user(user):
    user = User(**user)
    try:
        db.session.add(user)
        db.session.commit()
        return user.id
    except:
        return None

def queryAll():
    users = User.query.all()
    return users

def queryByPage(page, per_page=20):
    return User.query.paginate(page, per_page)
