#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To use a consistent encoding
from os import path
from codecs import open
from setuptools import find_packages, setup

# Always prefer setuptools over distutils
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dfuse',
    packages=find_packages(),
    version='0.0.5',
    description='Python wrapper around the dfuse.io API.',
    author='Cheese',
    author_email='ch33s3codes@gmail.com',
    url='https://github.com/th3ch33s3/dfuse-python',
    project_urls={
        'Bug Reports': 'https://github.com/th3ch33s3/dfuse-python/issues',
        'Buy me a coffee': 'https://github.com/th3ch33s3/dfuse-python#buy-me-a-coffee',
    },
    license='MIT License',
    install_requires=[
        'requests>=2.22.0',
        'requests_cache>=0.5.2',
        'websockets>=8.0.2',
        'grpcio>=1.23.0',
        'grpcio-tools>=1.23.0',
        'python-decouple>=3.1',
    ],
    keywords=['EOSIO', 'API', 'dfuse'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
