#!/usr/bin/env python3
__author__ = 'Administrator'
import optparse
import configparser


def readconfig(file='hello_config.ini'):
    config = configparser.ConfigParser()
    config.read(file)
    sections = config.sections()
    for section in sections:
        # uncomment line below to see how this config file is parsed
        # print Config.items(section)
        phrase = config.items(section)[0][1]
        return phrase


def main():
    p = optparse.OptionParser()
    p.add_option('--sysadmin', '-s')
    p.add_option('--config', '-c', action='store_true')
    p.set_defaults(sysadmin='BOFH')

    options, arguments = p.parse_args()
    if options.config:
        options.sysadmin = readconfig()
    print('Hello, %s' % options.sysadmin)


if __name__ == '__main__':
    main()