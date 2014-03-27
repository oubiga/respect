#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

import requests


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
LANGUAGES = (
    'javascript', 'ruby', 'python', 'java', 'php', 'c', 'c++', 'objective-c',
    'shell', 'c#')

GITHUB_SEARCH_USERS = 'https://api.github.com/search/users'


def spellchecker(word):
    """
    Looks for possible typos, i.e., deletion, insertion, transposition and
    alteration. If the target is 'audreyr': deletion is 'adreyr', insertion is
    'audreeyr', transposition is 'aurdeyr' and alteration is 'audriyr'.

    Returns a list of possible words sorted by matching the same length.
    """
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in ALPHABET if b]
    inserts = [a + c + b for a, b in splits for c in ALPHABET]
    guesses = set(deletes + transposes + replaces + inserts)
    sorted_guesses = sorted(guesses, key=lambda w: len(w) == len(word),
                            reverse=True)
    return sorted_guesses