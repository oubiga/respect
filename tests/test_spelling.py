#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_spelling
---------

Tests for `respect.spelling` module.
"""

import sys
import types
import requests

from respect import spelling

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestResultsStarredUsersByLanguages(unittest.TestCase):

    def test_generation_results_starred_users_languages(self):
        results = spelling.starred_users_by_languages()
        self.assertIsInstance(results, types.GeneratorType)


class TestGuessesSpellChecker(unittest.TestCase):

    def test_guesses_spellchecker(self):
        guesses = spelling.spellchecker('oubiga')
        self.assertIsInstance(guesses, list)


if __name__ == '__main__':
    unittest.main()