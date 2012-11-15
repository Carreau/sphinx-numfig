#!/usr/bin/env python

import sys, os, stat
# Locate sphinx
try:
  import sphinx
except:
  print "Sphinx not found.  Quitting."
  sys.exit(1)

print "Action is '" + sys.argv[1] + "'."
if sys.argv[1] == "build":
  print "Nothing to build.  Quitting."
  sys.exit(0)
elif sys.argv[1] == "install":
  pass
else:
  print sys.argv[1], "action not known.  Quitting."
  sys.exit(1)

# Remove the old installation
import shutil
import py_compile
sphinxdir = os.path.dirname(sphinx.__file__)
for abfile in "numfig.py", "numimg.py":
  olddst = os.path.join(sphinxdir, abfile)
  olddstc = os.path.join(sphinxdir, abfile + "c")
  sphinxextdir = os.path.join(sphinxdir, "ext")
  dst = os.path.join(sphinxextdir, abfile)
  dstc = os.path.join(sphinxextdir, abfile + "c")
  for f in [dst, olddst, dstc, olddstc]:
    try:
      os.remove(f)
    except:
      pass

# Assume we are in my directory
  print "Copying " + abfile + " to", dst
  shutil.copyfile(abfile, dst)

# Compile to bytecode
  print "Compiling", dst, "to bytecode."
  py_compile.compile(dst)

# Fix perms
  mode = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH
  print "Setting mode of", dst, "to 664."
  os.chmod(dst, mode)
  os.chmod(dstc, mode)

