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


class TestDispatchNotAllowedUsername(unittest.TestCase):

    def test_dispatch_not_allowed_username(self):
        pass


if __name__ == '__main__':
    unittest.main()