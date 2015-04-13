#!/usr/bin/env python3
__author__ = 'Administrator'

import optparse
import os


def main():
    p = optparse.OptionParser(description="Python 'ls' command clone",
                              prog='pyls',
                              version='0.1a',
                              usage='%prog [directory]')
    p.add_option("--verbose", '-v', action='store_true',
                 help='Enables Verbose Output',
                 default=False)
    options, arguments = p.parse_args()
    if len(arguments) == 1:
        path = arguments[0]
        for filename in os.listdir(path):
            if options.verbose:
                print('Filename: %s ' % filename)
            # elif options.quiet:
            #     pass
            else:
                print(filename)
    else:
        p.print_help()

if __name__ == '__main__':
    main()