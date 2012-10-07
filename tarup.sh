#!/bin/bash
#
# $Id$
#
ver=`svnversion -c . | sed -e 's/^.*://'`
nfdir=numfig-r$ver
cmd="mkdir -p $nfdir"
echo $cmd
$cmd
cp numfig.py install.sh $nfdir
tar czf $nfdir.tgz $nfdir
rm -rf $nfdir

