# -*- coding: utf-8 -*-


from webcore.utils.db import db
from webcore.modules.accounts.models import Role

'''
@param:role {}
'''
def add_role(role):
    role = Role(**role)
    try:
        db.session.add(role)
        db.session.commit()
        return role
    except Exception, e:
        print e
        return None

