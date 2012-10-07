#!/usr/bin/env python

import sys, os, stat
# Locate sphinx
try:
  import sphinx
except:
  print "Sphinx not found.  Quitting."
  sys.exit(1)

# Remove the old installation
sphinxextdir = os.path.dirname(sphinx.__file__)
dst = os.path.join(sphinxextdir, "numfig.py")
dstc = os.path.join(sphinxextdir, "numfig.pyc")
try:
  os.remove(dst)
except:
  pass
try:
  os.remove(dstc)
except:
  pass

# Assume we are in my directory
import shutil
shutil.copyfile("numfig.py", dst)

# Compile to bytecode
import py_compile
py_compile.compile(dst)

# Fix perms
mode = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH
os.chmod(dst, mode)
os.chmod(dstc, mode)
