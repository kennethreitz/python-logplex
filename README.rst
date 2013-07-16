Python-Logplex
==============

Python-Logplex is a fast & efficient client for sending log messages to
Heroku's `Logplex project <github.com/heroku/logplex>`_. It uses keep-alive
connections to enable high-throughput with little overhead.

Usage
-----

First, install the library::

    $ pip install logplex

Then, send some sample data::

    from logplex import Logplex

    logplex = Logplex(token='SECRETSAUCE')

    logplex.puts('\o/')

Enjoy!