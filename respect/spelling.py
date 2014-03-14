#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
LANGUAGES = (
    'javascript', 'ruby', 'python', 'java', 'php', 'c', 'c++', 'objective-c', 'shell', 'c#'
    )
BASE_URL = 'https://api.github.com/'
SEARCH_USERS_URL = '/search/users'


def starred_users_by_languages():
    """
    Generator which returns the most starred users by each language.
    Used in misspelling input before triger warning prompt to the user. 

    """
    pass

