Python-Logplex
==============

Python-Logplex is a fast & efficient client for sending log messages to
Heroku's [Logplex project](github.com/heroku/logplex). It uses keep-alive
connections to enable high-throughput with little overhead.

Usage
-----

Usage is fairly strait-forward::

    $ pip install logplex

Configure your static assets in ``settings.py``::

    from logplex import Logplex

    logplex = Logplex(token='SECRETSAUCE')

    logplex.puts('\o/')