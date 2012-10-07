#!/bin/bash

sphinxinit=`python -c "import sphinx; print sphinx.__file__"`
if test -z "$sphinxinit"; then
  echo "Sphinx not found.  Quitting."
  exit 1
fi
sphinxextdir=`dirname $sphinxinit`/ext
cp numfig.py $sphinxextdir

