#!/usr/bin/env python3
__author__ = 'Administrator'
import sys

# Python indexes start at Zero, so let`s not count the command itself which is
# sys.argv[0]

num_arguments = len(sys.argv) - 1
print('{} You typed in {} arguments'.format(sys.argv, num_arguments))