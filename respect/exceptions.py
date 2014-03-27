#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
respect.exceptions
------------------

All exceptions used in the Respect code base are defined here.
"""


class RespectException(Exception):
    """
    Base exception class. All Cookiecutter-specific exceptions should subclass
    this class.
    """


class AllowedLanguagesException(RespectException):
    """
    Raised when the language input is not defined by Github.

    """


class UnknownStausCodeException(RespectException):
    """
    Raseid when the status code is not 404, 403 or 200.

    """


class ConnectionErrorException(RespectException):
    """
    Raseid when "requests" is not able to establish the connection.

    """
