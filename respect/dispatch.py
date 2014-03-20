#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
from getpass import getpass
from datetime import datetime
import pprint

import requests


ENDPOINTS = {
    'username': 'https://api.github.com/users/',
    'stars': 'https://api.github.com/search/repositories?q=user:pydanny&page=1',
}


def dispatch(args, response, session=None):

    if args['stars']:
        print('in stars')
        user = args['<username>']
        result = []
        if session == None:
            last_stars_count = True
            rounds = 1
            content = True
            while content:
                built_url = 'https://api.github.com/search/repositories?q=user:%s&sort=stars&page=%s' % (user, str(rounds))
                r = requests.get(built_url)
                print(rounds)
                if r.json()['items']:
                    result.extend(r.json()['items'])
                else:
                    content = False
                    break
                rounds += 1
            print(result)
            stars = 0
            # TODO: sort by stars. reverse set to True is because of desc order.
            sorted_result = sorted(result, key=lambda x: x['stargazers_count'], reverse=True)
            for i in sorted_result:
                if args['--verbose']:
                    print('\nThe "'+i['name']+'"', 'repository has', i['stargazers_count'], "stars.", sep=" ")
                stars += int(i['stargazers_count'])
            print("\n"+user, "has", stars, 'stars in total.\n', sep=" ")


    elif args['repos']:
        if args['--language']:
            user = args['<username>']
            language = args['--language']
            result = []
            if session == None:
                last_stars_count = True
                rounds = 1
                content = True
                while content:
                    built_url = 'https://api.github.com/search/repositories?q=user:%s+language:%s&page=%s' % (user, language, str(rounds))
                    r = requests.get(built_url)
                    print(rounds)
                    if r.json()['items']:
                        result.extend(r.json()['items'])
                    else:
                        content = False
                        break
                    rounds += 1
                if result:
                    print(result)
                else:  
                    print('\n"'+user+'"', "doesn't have repositories written in", args['--language']+".\n", sep=" ")
                # TODO: respect bertez stars --verbose doesn't sort repositories by stars !!!!
                for i in result:
                    print('\n"'+i['name']+'"'+"\n", sep=" ")

        else:
            pass
    # TODO: catch everything even languages which don't exist, i.e., respect oubiga repos --language fakelanguage
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
