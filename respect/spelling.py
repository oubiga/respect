#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys 

import requests

if sys.version < '3':
    from urlparse import urljoin
else:
    from urllib.parse import urljoin


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
LANGUAGES = ('javascript', 'ruby', 'python', 'java', 'php', 'c', 'c++', 'objective-c', 'shell',
             'c#')
BASE_URL = 'https://api.github.com/'
SEARCH_USERS_URL = '/search/users'


def starred_users_by_languages():
    """
    Generator which returns the most starred users by each language.
    Used in misspelling input before triger warning prompt to the user. 

    """
    for language in LANGUAGES:
        #r = requests.get('https://api.github.com/search/users?q=language:%s&sort=stars&per_page=100' % (language,))

        params = {'q': "language:{0}".format(language), 'sort': 'stars', 'per_page': 100}
        try:
            r = requests.get(urljoin(BASE_URL, SEARCH_USERS_URL), params=params)
            yield r.json()['items']
        except Exception:
            # because of py3, getting the exception object through sys.exc_info()
            e = sys.exc_info(1)
            pass


def spellchecker(word):
    """
    Looks for possible typos, i.e., deletion, insertion, transposition and alteration.
    If the target is 'audreyr': deletion is 'adreyr', insertion is 'audreeyr', transposition is
    'aurdeyr' and alteration is 'audriyr'.
    Returns a list of possible words sorted by matching the same length.
    """
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces = [a + c + b[1:] for a, b in splits for c in ALPHABET if b]
    inserts = [a + c + b for a, b in splits for c in ALPHABET]
    guesses = set(deletes + transposes + replaces + inserts)
    sorted_guesses = sorted(guesses, key=lambda w: len(w) == len(word), reverse=True)
    return sorted_guesses
