#!/bin/bash

PYSITEPKGS_DIR=${PYSITEPKGS_DIR:-"/contrib/lib/python2.6/site-packages"}
SPHINX_EXT_DIR=
cp numfig.py $PYSITEPKGS_DIR/Sphinx-1.1.3-py2.6.egg/sphinx/ext
