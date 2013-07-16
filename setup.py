# -*- coding: utf-8 -*-
"""
Python-Logplex
==============

Python-Logplex is a fast & efficient client for sending log messages to
Heroku's `Logplex project <github.com/heroku/logplex>`_. It uses keep-alive
connections to enable high-throughput with little overhead.

Usage
-----

First, install the library.

    $ pip install logplex

Then, send some sample data::

    from logplex import Logplex

    logplex = Logplex(token='SECRETSAUCE')

    logplex.puts('\o/')

Enjoy!
"""

from setuptools import setup

setup(
    name='logplex',
    version='0.0.1',
    url='https://github.com/kennethreitz/logplex',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    description='.',
    long_description=__doc__,
    packages=['logplex', 'logplex.packages', 'logplex.packages.requests'],
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
