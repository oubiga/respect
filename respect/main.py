#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        respect <username> [--vcs=<name>]
        respect <username> <email>
        respect <username> <email> [--speed=<kn>]

    Options:
        -h, --help    Show this information.
        --vcs=<name>  Version control system to explore [default: 'gh'].

    '''
    args = docopt(parse_respect_args.__doc__, argv=args)
    return args


def main():
    """
    Main entry point for the `respect` command.

    """

    args = parse_respect_args(sys.argv[1:])
    r = requests.get(urljoin(GITHUB_USERS, args['<username>']))
    print args

    if r.status_code == 404 or r.status_code == 403:
        print 'input the username and password'
    elif r.status_code == 200:
        print "yes"
    else:
        print 'no'


if __name__ == '__main__':
    main()

