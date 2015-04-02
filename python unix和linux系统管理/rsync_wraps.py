#!/usr/bin/env python3
__author__ = 'Administrator'
# wraps up rsync to syncronize two directories
from subprocess import call
import sys

source = 'sync_dir_A'
target = 'sync_dir_B'
rsync = 'rsync'
arguments = '-a'
cmd = '%s %s %s %s' % (rsync, arguments, source, target)


def sync():
    ret = call(cmd, shell=True)
    if ret !=0:
        print('rsync failed')
        sys.exit(1)

sync()