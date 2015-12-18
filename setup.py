#!/usr/bin/env python
from distutils.core import setup


setup(
    name='ajenti-dev-multitool',
    version='1.0.14',
    install_requires=[
        'coloredlogs',
        'pyyaml',
    ],
    description='-',
    author='Eugene Pankov',
    author_email='e@ajenti.org',
    url='http://ajenti.org/',
    scripts=['ajenti-dev-multitool'],
)
