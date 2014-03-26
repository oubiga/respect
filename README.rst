=============
Cookiecutter
=============

.. image:: https://badge.fury.io/py/cookiecutter.png
    :target: http://badge.fury.io/py/cookiecutter

.. image:: https://travis-ci.org/audreyr/cookiecutter.png?branch=master
        :target: https://travis-ci.org/audreyr/cookiecutter

.. image:: https://pypip.in/d/cookiecutter/badge.png
        :target: https://crate.io/packages/cookiecutter?version=latest

.. image:: https://coveralls.io/repos/audreyr/cookiecutter/badge.png?branch=master
        :target: https://coveralls.io/r/audreyr/cookiecutter?branch=master


A command-line utility that creates projects from **cookiecutters** (project
templates), e.g. creating a Python package project from a Python package project template.

* Documentation: http://cookiecutter.rtfd.org
* GitHub: https://github.com/audreyr/cookiecutter
* Free software: BSD license
* PyPI: https://pypi.python.org/pypi/cookiecutter

.. image:: https://raw.github.com/audreyr/cookiecutter/aa309b73bdc974788ba265d843a65bb94c2e608e/cookiecutter_medium.png

Features
--------

Did someone say features?

* Cross-platform: Windows, Mac, and Linux are officially supported.

* Works with Python 2.6, 2.7, 3.3, and PyPy. *(But you don't have to know/write Python
  code to use Cookiecutter.)*

* Project templates can be in any programming language or markup format:
  Python, JavaScript, Ruby, CoffeeScript, RST, Markdown, CSS, HTML, you name
  it. You can use multiple languages in the same project template.

* Simple command line usage:

    .. code-block:: bash

        # Create project from the cookiecutter-pypackage.git repo template
        # You'll be prompted to enter values.
        # Then it'll create your Python package based on those values.
        $ cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
