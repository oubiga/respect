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

    def test_empty_qualifiers(self):
        qualifiers = utils.sanitize_qualifiers(repos=None, followers=None, language=None)
        self.assertEqual(qualifiers, '')


if __name__ == '__main__':
    unittest.main()