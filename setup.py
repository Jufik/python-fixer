#!/usr/bin/env python
import os
from setuptools import setup, find_packages


README = os.path.join(os.path.dirname(__file__), 'README.rst')

# when running tests using tox, README.md is not found
try:
    with open(README) as file:
        long_description = file.read()
except Exception:
    long_description = ''


setup(
    name='fixer',
    version='1.0.0',
    description='A python client for fixer io api',
    long_description=long_description,
    url='https://github.com/Jufik/python-fixer',
    author='Julien Kieffer TISSIER',
    author_email='julien.kieffer@gadz.org',
    maintainer='Fabian Affolter',
    maintainer_email='fabian@affolter-engineering.ch'
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='fixerio api currencies',
    packages=find_packages(),
    install_requires=['requests'],
    # test_suite='tests',
)
