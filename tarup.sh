#!/bin/bash
#
# $Id$
#
ver=`svnversion -c . | sed -e 's/^.*://'`
nfdir=sphinx_numfig-r$ver
cmd="mkdir -p $nfdir"
echo $cmd
$cmd
cp numfig.py setup.py $nfdir
cmd="tar czf $nfdir.tgz $nfdir"
echo $cmd
$cmd
rm -rf $nfdir

