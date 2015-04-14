#!/usr/bin/env python3
__author__ = 'Administrator'

import optparse
from subprocess import Popen, PIPE
import re


def main():
    p = optparse.OptionParser(description="Python wrapped snmpdf command",
                              prog='pysnmpdf',
                              version='0.1a',
                              usage='%prog machine')
    p.add_option('-c', '--community', help='snmp community string')
    p.add_option('-V', '--Version', help='snmp version to use')
    p.set_defaults(community='public', Version='2c')
    options, arguments = p.parse_args()
    SNMPDF = 'snmpdf'
    if len(arguments) == 1:
        machine = arguments[0]

        # Our new snmpdf action
        def parse():
            """Returns generator object with line from snmpdf """
            ps = Popen([SNMPDF, '-c', options.community,
                        '-v', options.Version, machine],
                       stdout=PIPE, stderr=PIPE)
            return ps.stdout

        # Generator Pipeline To search For Critical Items
        pattern = "9[0-9]%"
        outline = (line.split() for line in parse())  # remove carriage returns
        flag = (' '.join([a.decode() for a in row])
                for row in outline if re.search(pattern, row[-1].decode()))
        # patt search, join strings in list if match
        for line in flag:
            print('%s CRITICAL' % line)
            # Sample Return Value
            # Real Memory 2067636 1974120 93516 95% CRITICAL
    else:
        p.print_help()


if __name__ == '__main__':
    main()