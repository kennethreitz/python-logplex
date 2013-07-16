# -*- coding: utf-8 -*-
"""
Python-Logplex
==============

Python-Logplex is a fast & efficient client for sending log messages to
Heroku's `Logplex project <http://github.com/heroku/logplex>`_. It uses keep-alive
connections to enable high-throughput with little overhead.

Usage
-----

First, install the library::

    $ pip install logplex

Then, send some sample data::

    from logplex import Logplex

    logplex = Logplex(token='SECRETSAUCE')

    logplex.puts('\o/')


"""

from setuptools import setup

setup(
    name='logplex',
    version='0.0.2',
    url='https://github.com/kennethreitz/python-logplex',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    description='A Logplex client for Python.',
    long_description=__doc__,
    packages=[
        'logplex', 'logplex.packages', 'logplex.packages.requests',
        'logplex.packages.requests.packages',
        'logplex.packages.requests.packages.charade',
        'logplex.packages.requests.packages.urllib3',
        'logplex.packages.requests.packages.urllib3.packages',
        'logplex.packages.requests.packages.urllib3.contrib',
        'logplex.packages.requests.packages.urllib3.packages.ssl_match_hostname'
    ],
    zip_safe=False,
    install_requires=['requests'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
