#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='sphinx_numfig',
    version='0.1.1',
    description='Python Boilerplate contains all the boilerplate you need to create a Python package.',
    long_description=readme + '\n\n' + history,
    author='Matthias Bussonnier',
    author_email='bussonniermatthias@gmail.com',
    url='https://github.com/Carreau/sphinx_numfig',
    packages=[
        'sphinx_numfig',
    ],
    package_dir={'sphinx_numfig':
                 'sphinx_numfig'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='sphinx_numfig',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
