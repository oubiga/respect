#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
from getpass import getpass
from datetime import datetime
import pprint

import requests

from .utils import sanitize_qualifiers
from .utils import login


def dispatch(args, response=None, session=None):
    print(args)
    if args['<username>'] and args['bio']:
        try:
            user = args['<username>']
            output = response.json()
            created_at = datetime.strptime(output['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            joined = created_at.strftime("%b %d, %Y")
            if output['name']:

                print("\n{0} (from {1}), aka @{2}, joined Github on {3}, has {4} follower{5}, " 
                      "is following {6} {7} and has {8} public repositories.\n"
                      .format(output['name'].title().encode('utf-8'),
                              output['location'].encode('utf-8') if output['location'] else 'somewhere', 
                              output['login'], joined, output['followers'],
                              "s"[int(output['followers'])==1:], output['following'],
                              'person' if abs(int(output['following'])) == 1 else 'people',
                              output['public_repos']))
            else:
                print("\n@{0} joined Github on {1}, has {2} follower{3}, is following {4} {5} and "
                      "has {6} public repositories.\n".format(output['login'], joined,
                      output['followers'], "s"[int(output['followers'])==1:], output['following'],
                      'person' if abs(int(output['following'])) == 1 else 'people', 
                      output['public_repos']))
        except KeyError as e:
            print("\n@{0} name is blank.\n".format(user,))

    elif args['<username>'] and args['stars']:
        user = args['<username>']
        result = []
        if session == None:
            last_stars_count = True
            rounds = 1
            content = True
            while content:
                built_url = \
                    'https://api.github.com/search/repositories?q=user:%s&sort=stars&page=%s' \
                    % (user, str(rounds))
                r = requests.get(built_url)
                if r.json().get('items', False):
                    result.extend(r.json()['items'])
                else:
                    content = False
                    break
                rounds += 1
            stars = 0
            sorted_result = sorted(result, key=lambda x: x['stargazers_count'], reverse=True)
            if args['--verbose']:
                print("The stars grouped into repositories:\n")
            for i in sorted_result:
                if args['--verbose']:
                    print("\"{0}\" ({1}) repository has {2} stars."
                          .format(i['name'],
                                  i['language'] if i['language'] else "no language assigned",
                                  i['stargazers_count']))
                stars += int(i['stargazers_count'])
            print("\n@"+user, "has", stars, 'stars in total.\n', sep=" ")

    elif args['<username>'] and args['repos']:
        sanitized_qualifiers = sanitize_qualifiers(language=args['--language'])
        qualifiers = 'user:' + args['<username>'] + ' ' + sanitized_qualifiers
        params = {'q': qualifiers, 'sort': 'stars'}
        if not session:
            session = login(401, args)
        r = session.get('https://api.github.com/search/repositories', params=params)
        if not r.json()['total_count']:
            print("\nThere are not repositories that match your search.\n")
            return
        else:
            print("\nThe repositories that match your search are:\n")
        items = r.json().get('items', None)
        for i in items:
            try:
                print('"'+i['name']+'"', '('+i['language']+')', 'has', str(i['stargazers_count']),
                      'stars.')
                if args['--verbose'] and i['description']:
                    print(i['description']+'\n')
                elif args['--verbose']:
                    print("There is no description."+'\n')
                else:
                    continue
            except (TypeError, KeyError) as e:
                pass
        print('')
        return

    elif args['<username>'] and not args['stars']:
        sanitized_qualifiers = sanitize_qualifiers(args['--repos'], args['--followers'],
                                                   args['--language'])
        qualifiers = args['<username>'] + ' ' + sanitized_qualifiers
        params = {'q': qualifiers, 'sort': 'followers'}
        if not session:
            session = login(401, args)
        r = session.get('https://api.github.com/search/users', params=params)
        if not r.json()['total_count']:
            print("\nThere are not results that match your search.\n")
            return
        else:
            print("The users related to \"{0}\" are:\n".format(args['<username>']))
        items = r.json().get('items', None)
        for i in items:
            print("@"+i['login'])
        print('')
        return

    else:
        print("Sorry, no results here. Try \"$ respect -h\" for help.")

