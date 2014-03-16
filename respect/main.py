#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
from getpass import getpass

from docopt import docopt 
import requests

from .spelling import spellchecker

if sys.version < '3':
    from urlparse import urljoin
else:
    from urllib.parse import urljoin

GITHUB_BASE_URL = 'https://api.github.com'
GITHUB_USERS = urljoin(GITHUB_BASE_URL, 'users')
GITHUB_USER = 'user'

def parse_respect_args(args):
    '''
    Respect

    Usage:
        respect <username> [--pages=<num>]
        respect <username> [stars | starred | repos | languages | followers | following] [--filter=<qualifier>] [--pages=<num>]
        respect <username> <language>... [--pages=<num>]
        respect <username> <repo>... [--order=<ord>] [--pages=<num>]
        respect <username> <email>
        respect <username> <email> [--speed=<kn>]

    Options:
        -h, --help              Show this information.
        --filter=<qualifier>    Filter the result [default: None].
        --pages=<num>           Number of pages to print [default: 20].
        --order=<ord>           The sort order if sort parameter is provided [default: 'desc'].

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
        print('input the username and password')
    elif r.status_code == 200:
        print("yes")
    else:
        print('no')


if __name__ == '__main__':
    main()

