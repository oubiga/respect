#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from getpass import getpass

from docopt import docopt 


def parse_respect_args(args):
    DOC = '''
            Respect

            Usage:
                respect get <username> [--vcs=<name>]
                respect <username> <email>
                respect <username> <email> [--speed=<kn>]

            Options:
                -h, --help    Show this information.
                --vcs=<name>  Version control system to explore [default: 'gh'].

            '''
    args = docopt(DOC, argv=args)
    return args


def main():
    """
    Main entry point for the `respect` command.

    """

    args = parse_respect_args(sys.argv[1:])
    return args


if __name__ == '__main__':
    main()

