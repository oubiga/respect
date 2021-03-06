#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dispatch
-------------

Tests for `respect.dispatch` module.
"""

import sys
import types
import requests

from respect import dispatch

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestDispatchBioNotResponseProvided(unittest.TestCase):

    def test_dispatch_bio_not_response_provided(self):
        args = {'--followers': '', '--help': False, '--language': '', '--repos': '',
                '--verbose': False, '<username>': 'oubiga', 'bio': True, 'repos': False,
                'stars': False}
        output = dispatch.dispatch(args, response=None, session=None)
        self.assertEqual(output, None)


class TestDispatchStarsNotResponseProvided(unittest.TestCase):

    def test_dispatch_stars_not_response_provided(self):
        args = {'--followers': '', '--help': False, '--language': '', '--repos': '',
                '--verbose': False, '<username>': 'oubiga', 'bio': False, 'repos': False,
                'stars': True}
        output = dispatch.dispatch(args, response=None, session=None)
        self.assertEqual(output, None)


class TestDispatchReposInvalidSession(unittest.TestCase):

    def test_dispatch_repos_invalid_session(self):
        session = requests.Session()
        args = {'--followers': '', '--help': False, '--language': '', '--repos': '',
                '--verbose': False, '<username>': 'oubiga', 'bio': False, 'repos': True,
                'stars': False}
        output = dispatch.dispatch(args, response=None, session=session)
        self.assertEqual(output, None)


class TestDispatchUsernameInvalidSession(unittest.TestCase):

    def test_dispatch_username_invalid_session(self):
        session = requests.Session()
        args = {'--followers': '', '--help': False, '--language': '', '--repos': '',
                '--verbose': False, '<username>': 'oubiga', 'bio': False, 'repos': False,
                'stars': False}
        output = dispatch.dispatch(args, response=None, session=session)
        self.assertEqual(output, None)


class TestDispatchBadResponse(unittest.TestCase):

    def test_dispatch_bad_response(self):
        response = requests.get('https://api.github.com/user')
        args = {'--followers': '', '--help': False, '--language': '', '--repos': '',
                '--verbose': False, '<username>': 'oubiga', 'bio': True, 'repos': False,
                'stars': False}
        output = dispatch.dispatch(args, response=response)
        self.assertEqual(output, None)


if __name__ == '__main__':
    unittest.main()