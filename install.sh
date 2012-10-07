#!/bin/bash

# Locate sphinx
sphinxinit=`python -c "import sphinx; print sphinx.__file__"`
if test -z "$sphinxinit"; then
  echo "Sphinx not found.  Quitting."
  exit 1
fi

# Copy file to extensions directory
if [[ `uname` =~ CYGWIN ]]; then
  sphinxinit=`cygpath -au "$sphinxinit"`
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
numfigfile="${sphinxextdir}/numfig.py"
if [[ `uname` =~ CYGWIN ]]; then
  numfigfile=`cygpath -aw "$numfigfile" | sed -e 's/\\/\\\\/g'`
# May need more backslashes here
fi
echo "numfigfile = $numfigfile."
cmd="python -c \"import py_compile;  py_compile.compile('${numfigfile}')\""
echo "$cmd"
eval "$cmd"
# Fix perms
chmod 664 ${sphinxextdir}/numfig.py*

