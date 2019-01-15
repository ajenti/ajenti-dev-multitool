#!/usr/bin/env python
from setuptools import setup


setup(
    name='ajenti-dev-multitool',
    version='1.1.8',
    install_requires=[
        'coloredlogs',
        'pyyaml',
        'gevent',
    ],
    description='-',
    author='Eugene Pankov',
    author_email='e@ajenti.org',
    url='http://ajenti.org/',
    scripts=['ajenti-dev-multitool'],
)
