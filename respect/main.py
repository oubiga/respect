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
from .utils import login

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
        respect <username> [--pages=<num>] [--repos=<rep>] [--followers=<foll>][--language=<lang>]
        respect <username> stars [--verbose]
        respect <username> repos [--language=<lang>]
        respect <username> starred [--filter=<qualifier>] [--pages=<num>]
        respect <username> <email>
        respect -h | --help

    Options:
        -h, --help                          Shows this help information.
        --filter=<qualifier>                Filters the result [default: None].
        --repos=<rep>                       Number of repositories [default: None].
        --followers=<foll>                  Number of follwers [default: None].
        --language=<lang>                   Filters by the repository language [default: None].
        --pages=<num>                       Number of pages to print [default: 20].
        --verbose                           Prints detailed information.

    '''
    args = docopt(parse_respect_args.__doc__, argv=args)
    return args


def main():
    """
    Main entry point for the `respect` command.

    """
    args = parse_respect_args(sys.argv[1:])
    print("processing...")
    r = requests.get(urljoin(GITHUB_USERS, args['<username>']))
    # print(args)

    if r.status_code == 404 or r.status_code == 403:
        session = login(401, args=args)
        return dispatch(args, r, session)

    elif r.status_code == 200:
        return dispatch(args, response=r)
    else:
        print('no')


if __name__ == '__main__':
    main()


















