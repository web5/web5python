# -*- coding: utf-8 -*-

import logging
from web.core.app.accounts import user

logger = logging.getLogger()

def get_current_user():
    from flask.ext.security import current_user
    try:
        if not current_user.is_authenticated():
            return None
    except RuntimeError:
        pass

    try:
        return user.queryUserById(current_user.id)
    except Exception as e:
        logger.warning('No user found : %s ' % e.message)
        return None


   :
