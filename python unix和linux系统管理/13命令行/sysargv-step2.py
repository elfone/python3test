#!/usr/bin/env python3
__author__ = 'Administrator'
import sys

num_arguments = len(sys.argv) - 1
# If there are no arguments to the command, send a message to standard error.
if num_arguments == 0:
    sys.stderr.write('Hey, type in an option silly\n')
else:
    print('{} You typed in {} arguments'.format(sys.argv, num_arguments))