#!/usr/bin/env python3

activate_this = '/var/www/bot/venv/bin/activate_this.py'
with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/bot')

from bot import app as application
