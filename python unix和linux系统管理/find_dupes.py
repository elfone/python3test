#!/usr/bin/env python3
__author__ = 'Administrator'
from checksum import create_checksum
from diskwalk_api import diskwalk
from os.path import getsize


def finddupes(path='.'):
    dup = []
    record = {}
    d = diskwalk(path)
    files = d.enumeratePaths()
    for file in files:
        compound_key = (getsize(file), create_checksum(file))
        if compound_key in record:
            dup.append(file)
        else:
            # print('Creating compound key record:{} {}'.format(file, compound_key))
            record[compound_key] = file
    return dup

if __name__ == '__main__':
    dupes = finddupes()
    for dup in dupes:
        print('Duplicate: %s' % dup)