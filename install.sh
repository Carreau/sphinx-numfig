#!/bin/bash

# Locate sphinx
sphinxinit=`python -c "import sphinx; print sphinx.__file__"`
if test -z "$sphinxinit"; then
  echo "Sphinx not found.  Quitting."
  exit 1
fi
sphinxextdir=`dirname $sphinxinit`/ext
cmd="rm -f $sphinxextdir/numfig.py*"
echo $cmd
$cmd
mydir=`dirname $0`
mydir=`(cd $mydir; pwd -P)`
cmd="cp $mydir/numfig.py $sphinxextdir"
echo $cmd
$cmd
# Compile to bytecode
cmd="python -c \"import py_compile;  py_compile.compile('${sphinxextdir}/numfig.py')\""
echo "$cmd"
eval "$cmd"
# Fix perms
chmod 664 ${sphinxextdir}/numfig.py*

