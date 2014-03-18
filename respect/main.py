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


def dispach(args, response, session=None):

    if args['stars']:
        print('in stars')
        user = args['<username>']
        result = []
        if session == None:
            last_stars_count = True
            rounds = 1
            content = True
            while content:

                built_url = 'https://api.github.com/search/repositories?q=user:%s&page=%s' % (user, str(rounds))
                r = requests.get(built_url)
                print(rounds)
                try:
                    result.extend(r.json()['items'])
                except IndexError:
                    content = False
                    break
                content = r.json()['items']
                # last_stars_count = int(r.json()['items'][-1]['stargazers_count'])
                rounds += 1
                # return last_stars_count
            print(result)
            stars = 0
            # TODO: respect bertez stars --verbose doesn't sort repositories by stars !!!!
            for i in result:
                if args['--verbose']:
                    print('"'+i['name']+'"', 'repository has', i['stargazers_count'], "stars.", sep=" ")
                stars += int(i['stargazers_count'])
            print(user, "has", stars, 'stars', sep=" ")

    else:

        try:
            print(response)
            user = args['<username>']
            output = response.json()
            created_at = datetime.strptime(output['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            joined = created_at.strftime("%b %d, %Y")
            pprint.pprint(output, indent=4, depth=1)
            if output['name']:

                print("\n{0}, aka {1}, joined Github on {2}, has {3} follower{4}, is following {5} {6} " 
                      "and has {7} public repositories.\n".format(output['name'].title().encode('utf-8'), 
                      output['login'], joined, output['followers'], "s"[int(output['followers'])==1:], 
                      output['following'], 'person' if abs(int(output['following'])) == 1 else 'people',
                      output['public_repos']))
            else:
                print("\n{0} joined Github on {1}, has {2} follower{3}, is following {4} {5} and "
                      "has {6} public repositories.\n".format(output['login'], joined,
                      output['followers'], "s"[int(output['followers'])==1:], output['following'],
                      'person' if abs(int(output['following'])) == 1 else 'people', 
                      output['public_repos']))


        except KeyError as e:
            # the user arigo doesn't have the name attribute
            print("\n{0} joined Github on {1}, has {2} follower{3}, is following {4} {5} and " 
                  "has {6} public repositories.\n".format(output['login'], joined,
                  output['followers'], "s"[int(output['followers'])==1:], output['following'], 
                  'person' if abs(int(output['following'])) == 1 else 'people',
                  output['public_repos']))



def parse_respect_args(args):
    '''
    Respect

    Usage:
        respect <username> [--pages=<num>]
        respect <username> stars [--verbose]
        respect <username> [starred | repos | languages | followers | following] [--filter=<qualifier>] [--pages=<num>]
        respect <username> <language>... [--pages=<num>]
        respect <username> <repo>... [--order=<ord>] [--pages=<num>]
        respect <username> <email>
        respect <username> <email> [--speed=<kn>]

    Options:
        -h, --help              Show this information.
        --filter=<qualifier>    Filter the result [default: None].
        --pages=<num>           Number of pages to print [default: 20].
        --verbose       Prints more information.
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
        return dispach(args, r, s)


    elif r.status_code == 200:
        print("yes")
        return dispach(args, r)
    else:
        print('no')


if __name__ == '__main__':
    main()


















