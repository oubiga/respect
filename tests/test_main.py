#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_main
---------

Tests for `respect.main` module.
"""

import sys

from respect import main

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestArgParsing(unittest.TestCase):

    def test_parse_respect_args(self):
        args = main.parse_respect_args(['oubiga', 'oubiga@yahoo.es'])
        self.assertEqual(args['<username>'], 'oubiga')
        self.assertEqual(args['<email>'], 'oubiga@yahoo.es')
        self.assertIsInstance(args, dict)



if __name__ == '__main__':
    unittest.main()