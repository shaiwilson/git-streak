#!/usr/bin/env python
# author: shai wilson

import subprocess, shlex
import sys, os.path
import logging as logger
import argparse
import time
import re

parser = argparse.ArgumentParser(
    description='Show the date of the most recent commit inside '
                'a git directory. Useful when attempting to maintain'
                'A github streak.  '
                'Current directory must be inside work git tree')

parser.add_argument('pathspec',
                    nargs='*', default=[os.path.curdir],
                    help='only modify paths (dirs or files) matching PATHSPEC, '
                        'absolute or relative to current directory. '
                        'Default is current directory')

args = parser.parse_args()

# Find repo's top level.
try:
    workdir = os.path.abspath(subprocess.check_output(shlex.split(
                    'git rev-parse --show-toplevel')).strip())
except subprocess.CalledProcessError as e:
    sys.exit(e.returncode)


# List files matching user pathspec, relative to current directory
# git commands always print paths relative to work tree root
filelist = set()
for path in args.pathspec:

    # file or symlink (to file, to dir or broken - git handles the same way)
    if os.path.isfile(path) or os.path.islink(path):
        filelist.add(os.path.relpath(path, workdir))

    # dir
    elif os.path.isdir(path):
        for root, subdirs, files in os.walk(path):
            if '.git' in subdirs:
                subdirs.remove('.git')

            for file in files:
                filelist.add(os.path.relpath(os.path.join(root, file), workdir))


# Process the log until all files are 'touched'
def parselog(filterlist=[]):
    gitobj = subprocess.Popen(shlex.split('git log -1 --format="%ad" -- $filename') +
                              ([]) + filterlist,
                              stdout=subprocess.PIPE)
    mtime = 0
    for line in gitobj.stdout:
        line = line.strip()
        # Blank line between Date and list of files
        if not line: continue
        mtime = line
        print "Date is", mtime
        # All files done?
        if not filelist:
            break

# Missing files
if filelist:
    filterlist = list(filelist)
    for i in range(0, len(filterlist), 100):
        parselog(filterlist=filterlist[i:i+100])



