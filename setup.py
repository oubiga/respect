#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()

requirements = ['docopt>=0.6.1', 'requests>=2.2.1']
test_requirements = []

if sys.version < '3':
    test_requirements.append('mock')


setup(
    name='respect',
    version='0.0.1',
    description="A command-line tool to interact with the Github API, \
        e.g. looking for user's stars who is interesting for you.",
    long_description=readme,
    author='Pablo Oubiña',
    author_email='oubiga@yahoo.es',
    url='https://github.com/oubiga/respect',
    packages=[
        'respect',
    ],
    package_dir={'respect': 'respect'},
    entry_points={
        'console_scripts': [
            'respect = respect.main:main',
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license='BSD',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    keywords='respect, Python, stars, user, github, \
        repository, code, software',
    test_suite='tests',
    tests_require=test_requirements
)