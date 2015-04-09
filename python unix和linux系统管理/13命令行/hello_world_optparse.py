#!/usr/bin/env python3
__author__ = 'Administrator'
import optparse


def main():
    p = optparse.OptionParser()
    p.add_option('--sysadmin', '-s', default='BOFH')
    options, arguments = p.parse_args()
    print('Hello, %s' % options.sysadmin)


if __name__ == '__main__':
    main()