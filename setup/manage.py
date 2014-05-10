#!/etc/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from webcore.app import create_app


app = create_app()



manager = Manager(app)

if __name__ == '__main__':
    manager.run()
