#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
from getpass import getpass
from datetime import datetime
import pprint

from docopt import docopt 
import requests

from .spelling import spellchecker
from .dispatch import dispatch

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


def parse_respect_args(args):
    '''
    Respect

    Usage:
        respect <username> [--pages=<num>]
        respect <username> stars [--verbose]
        respect <username> repos [--language=<lang>]
        respect <username> [starred | followers | following] [--filter=<qualifier>] [--pages=<num>]
        respect <username> <language>... [--pages=<num>]
        respect <username> <repo>... [--order=<ord>] [--pages=<num>]
        respect <username> <email>
        respect <username> <email> [--speed=<kn>]

    Options:
        -h, --help                          Show this information.
        --filter=<qualifier>                Filter the result [default: None].
        --language=<lang>                   Repository language [default: ].
        --pages=<num>                       Number of pages to print [default: 20].
        --verbose                           Prints more information.
        --order=<ord>                       The sort order if sort parameter is provided [default: 'desc'].

    '''
    args = docopt(parse_respect_args.__doc__, argv=args)
    return args


def main():
    """
    Main entry point for the `respect` command.

    """

    args = parse_respect_args(sys.argv[1:])
    r = requests.get(urljoin(GITHUB_USERS, args['<username>']))
    print(args)

    if r.status_code == 404 or r.status_code == 403:
        print('Input the username and password')
        prompt = "Your username: "

        if PY3:
            username = input(prompt.encode('utf-8'))
        else:
            username = input(prompt.encode('utf-8')).decode('utf-8')

        password = getpass("Your password: ")

        s = requests.Session()
        s.auth = (username, password)
        print(args['<username>'])
        r = s.get(urljoin(GITHUB_USERS, args['<username>']))
        print(r)
        return dispatch(args, r, s)


    elif r.status_code == 200:
        print("yes")
        return dispatch(args, r)
    else:
        print('no')


if __name__ == '__main__':
    main()


















