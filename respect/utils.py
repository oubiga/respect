#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
from getpass import getpass
from datetime import datetime

from docopt import docopt 
import requests

PY3 = sys.version > '3'

if PY3:
    pass
else:
    input = raw_input


if sys.version < '3':
    from urlparse import urljoin
else:
    from urllib.parse import urljoin

GITHUB_BASE_URL = 'https://api.github.com'
GITHUB_USERS = 'https://api.github.com/users/'
GITHUB_USER = 'user'


def login(status, args=None):
    print('\nThis request needs user authentication:')
    message = None
    while status == 401:
        if message:
            print(message)
        prompt = "Github username: "
        if PY3:
            username = input(prompt.encode('utf-8'))
        else:
            username = input(prompt.encode('utf-8')).decode('utf-8')

        password = getpass("Github password (hidden): ")

        s = requests.Session()
        s.auth = (username, password)
        r = s.get(urljoin(GITHUB_USERS, args['<username>']))
        status = r.status_code
        if status == 404:
            break
        print("status is: ", status, sep=' ')
        message = '\nIncorrect username or password. Try again:'

    return s