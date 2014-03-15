#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_main
---------

Tests for `respect.main` module.
"""

import sys
import types
import requests

from respect import main

if sys.version < '3':
    from urlparse import urljoin
else:
    from urllib.parse import urljoin

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest

GITHUB_BASE_URL = 'https://api.github.com'
GITHUB_USER = 'user'


class TestArgParsing(unittest.TestCase):

    def test_parse_respect_args(self):
        args = main.parse_respect_args(['oubiga', 'oubiga@yahoo.es'])
        self.assertEqual(args['<username>'], 'oubiga')
        self.assertEqual(args['<email>'], 'oubiga@yahoo.es')
        self.assertIsInstance(args, dict)


class TestGithubBasicAuthentication(unittest.TestCase):

    def test_github_basic_authenthication(self):
        r = requests.get(GITHUB_BASE_URL)
        self.assertEqual(r.status_code, 200)


class TestGithubBadBasicAuthentication(unittest.TestCase):

    def test_github_bad_basic_authenthication(self):
        r = requests.get(urljoin(GITHUB_BASE_URL, GITHUB_USER), auth=('oubiga', 'xxxxxxxx'))
        self.assertEqual(r.status_code, 401)


class TestGithubGetAuthenticatedUser(unittest.TestCase):

    def test_github_get_not_authenthicated_user(self):
        r = requests.get(urljoin(GITHUB_BASE_URL, GITHUB_USER))
        self.assertEqual(r.status_code, 401)


if __name__ == '__main__':
    unittest.main()


