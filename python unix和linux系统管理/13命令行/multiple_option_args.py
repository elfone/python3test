#!/usr/bin/env python3
__author__ = 'Administrator'

import optparse
import os


def main():
    p = optparse.OptionParser(description="Python 'ls' command clone",
                              prog='pyls',
                              version='0.1a',
                              usage='%prog [directory]')
    p.add_option('--dir', action='store', dest='dir', nargs=2)
    options, arguments = p.parse_args()
    if options.dir:
        for dir in options.dir:
            print('Listing of %s:\n' % dir)
            for filename in os.listdir(dir):
                print(filename)
    else:
        p.print_help()

if __name__ == '__main__':
    main()