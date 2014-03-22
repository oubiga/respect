#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import time
from threading import Thread, Lock
import itertools


import requests

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
PERMUTATIONS = map(''.join, itertools.chain(itertools.product(ALPHABET, ALPHABET)))

GITHUB_SEARCH_USERS = 'https://api.github.com/search/users'

lock = Lock()

results = []

class GetUrlThread(Thread):
    def __init__(self, url, params, session):
        self.url = url 
        self.params = params
        self.session = session
        super(GetUrlThread, self).__init__()

    def run(self):
        lock.acquire()

        resp = self.session.get(self.url, params=self.params)
        print(resp.url, resp.status_code)
        results.append(resp.json())
        # print(self.results)
        lock.release()


def get_responses(session, sanitized_qualifiers):
    print('processing...')
    start = time.time()
    threads = []
    sanitized_qualifiers = sanitized_qualifiers
    
    for letter in PERMUTATIONS:
        qualifiers = letter + ' ' + sanitized_qualifiers
        params = {'q': qualifiers, 'sort': 'followers'}
        url_built = GITHUB_SEARCH_USERS
        t = GetUrlThread(url_built, params, session)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    #print("Elapsed time: %s" % (time.time()-start))
    #print(results)
    return results



































