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


class TestInvalidUsername(unittest.TestCase):

    def test_dot_invalid_username(self):
        validation = utils.validate_username('ou.bi.ga')
        self.assertFalse(validation)

    def test_underscore_invalid_username(self):
        validation = utils.validate_username('ou_bi_ga')
        self.assertFalse(validation)


if __name__ == '__main__':
    unittest.main()