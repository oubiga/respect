#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_utils
----------

Tests for `respect.utils` module.
"""

import sys
import types
import requests

from respect import utils

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestEmptyQualifiers(unittest.TestCase):

    def test_none_qualifiers(self):
        qualifiers = utils.sanitize_qualifiers(repos=None, followers=None, language=None)
        self.assertEqual(qualifiers, '')

    def test_empty_repos(self):
        qualifiers = utils.sanitize_qualifiers(repos='', followers=None, language=None)
        self.assertEqual(qualifiers, '')

    def test_empty_followers(self):
        qualifiers = utils.sanitize_qualifiers(repos=None, followers='', language=None)
        self.assertEqual(qualifiers, '')


class TestSanitizedQualifiers(unittest.TestCase):

    def test_sanitized_repos_qualifiers(self):
        qualifiers = utils.sanitize_qualifiers(repos='+20')
        self.assertEqual(qualifiers, 'repos:>20 ')

    def test_sanitized_followers_qualifiers(self):
        qualifiers = utils.sanitize_qualifiers(followers='-20')
        self.assertEqual(qualifiers, 'followers:<20 ')

    def test_sanitized_language_qualifiers(self):
        qualifiers = utils.sanitize_qualifiers(language='python')
        self.assertEqual(qualifiers, 'language:python ')


class TestInvalidUsername(unittest.TestCase):

    def test_dot_invalid_username(self):
        validation = utils.validate_username('ou.bi.ga')
        self.assertFalse(validation)

    def test_underscore_invalid_username(self):
        validation = utils.validate_username('ou_bi_ga')
        self.assertFalse(validation)


class TestLogin(unittest.TestCase):

    def test_invalid_login(self):
        output = utils.login(404, {'<username>': 'oubiga'})
        self.assertIsInstance(output, requests.Session)


if __name__ == '__main__':
    unittest.main()