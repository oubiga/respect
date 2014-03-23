#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
from getpass import getpass
from datetime import datetime
import re

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

ALLOWED_LANGUAGES = ['abap', 'actionscript', 'ada', 'agda', 'antlr', 'apex', 'applescript', 'arc',
'arduino', 'asp', 'assembly', 'augeas', 'autohotkey', 'autoit', 'awk', 'blitzbasic', 'bluespec',
'boo', 'brightscript', 'bro', 'c', 'c#', 'c++', 'ceylon', 'clean', 'clips', 'clojure', 'cobol',
'coffeescript', 'coldfusion', 'coq', 'crystal', 'css', 'd', 'dart', 'dm', 'dot', 'dylan', 'ec',
'eiffel', 'elixir', 'elm', 'erlang', 'f#', 'factor', 'fancy', 'fantom', 'forth', 'fortran', 'glyph',
'go', 'gosu', 'groovy', 'haskell', 'haxe', 'idl', 'idris', 'io', 'ioke', 'j', 'java', 'javascript',
'julia', 'kotlin', 'krl', 'lasso', 'livescript', 'logos', 'logtalk', 'lua', 'm', 'markdown',
'matlab', 'max', 'mirah', 'monkey', 'moonscript', 'nemerle', 'nesc', 'netlogo', 'nimrod', 'nu',
'objective-c', 'objective-j', 'ocaml', 'omgrofl', 'ooc', 'opa', 'oxygene', 'parrot', 'pascal',
'perl', 'php', 'pike', 'pogoscript', 'powershell', 'processing', 'prolog', 'puppet', 'python', 'r',
'racket', 'rdoc', 'realbasic', 'rebol', 'robotframework', 'rouge', 'ruby', 'rust', 'scala',
'scheme', 'scilab', 'self', 'shell', 'slash', 'smalltalk', 'squirrel', 'supercollider', 'tcl',
'tex', 'turing', 'txl', 'typescript', 'unrealscript', 'vala', 'verilog', 'vhdl', 'viml', 'volt',
'wisp', 'xbase', 'xc', 'xml', 'xproc', 'xquery', 'xslt', 'xtend']


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
        message = 'Incorrect username or password. Try again:'

    return s


def sanitize_qualifiers(repos=None, followers=None, language=None):
    '''
    qualifiers = c repos:+42 followers:+1000 language:
    params = {'q': 'tom repos:>42 followers:>1000'}
    '''
    try:
        repos = repos
        print(repos, 'nooo')
    except ValueError as e:
        repos = None
    except TypeError as e:
        repos = None

    try:
        followers = followers
    except ValueError as e:
        followers = None
    except TypeError as e:
        followers = None

    qualifiers = ''

    if repos:
        qualifiers += 'repos:{} '.format(repos)

    if followers:
        qualifiers += 'followers:{} '.format(followers)

    if language in ALLOWED_LANGUAGES:
        qualifiers += 'language:{} '.format(language)
    else:
        print(language.title(), "is not a allowed language.")
        # TODO: handle this exception !!!!!!
        raise Exception 

    print(qualifiers, 'yes')
    return qualifiers.replace('+', '>').replace('-', '<')



def validate_username(username):
    """
    Returns True if the username matches Github constraints.
    Valid usernames: oubiga, oubiga2000, oubi-ga, Oub75igA
    Invalid usernames: -oubiga, oub_iga, ou.biga
    """
    result = re.match(r"^[^-][-a-zA-Z0-9]+$", username)
    return not result == None

