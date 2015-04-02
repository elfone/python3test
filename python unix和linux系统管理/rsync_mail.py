#!/usr/bin/env python3
__author__ = 'Administrator'
# wraps up rsync to synchronize two directories
from subprocess import call
import sys
import time

"""this motivated rsync tried to synchronize forever"""

source = 'sync_dir_A/'  # Note the trailing slash
target = 'sync_dir_B'
rsync = 'rsync'
arguments = '-av'
cmd = '%s %s %s %s' % (rsync, arguments, source, target)


def sync():
    while True:
        ret = call(cmd, shell=True)
        if ret != 0:
            print('resubmitting rsync')
            time.sleep(3)
        else:
            print('rsync was succesful')
            call("echo 'jobs done'|mail -s 'jobs done' test@123.com ", shell=True)
            sys.exit(0)

sync()