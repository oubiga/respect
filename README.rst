.. image:: https://raw.githubusercontent.com/oubiga/respect/master/respect-logo.png

.. image:: https://badge.fury.io/py/respect.png
        :target: http://badge.fury.io/py/respect

.. image:: https://travis-ci.org/oubiga/respect.png?branch=master
        :target: https://travis-ci.org/oubiga/respect

.. image:: https://coveralls.io/repos/oubiga/respect/badge.png?branch=master
        :target: https://coveralls.io/r/oubiga/respect?branch=master


A command-line tool to interact with the Github API. Getting to know software developers you **respect**

.. code-block:: shell

    $ pip install --pre respect

.. code-block:: shell

    $ respect audreyr bio

.. code-block:: shell

    Audrey Roy (from Inland Empire, CA), aka @audreyr, joined Github on Apr 17, 2009,
    has 389 followers, is following 210 people and has 90 public repositories.

.. code-block:: shell

    $ respect audreyr stars

.. code-block:: shell

    @audreyr has 5896 stars in total.

.. code-block:: shell

    $ respect Roy --repos +10 --followers +200 --language python

.. code-block:: shell

    This request needs user authentication:

    Github username: oubiga
    Github password (hidden):
    The users related to "Roy" are:

    @audreyr
    @binux
