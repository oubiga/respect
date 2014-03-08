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


if __name__ == '__main__':
    unittest.main()