#!/usr/bin/env python3
__author__ = 'Administrator'

import hashlib


def create_checksum(path):
    """
    Reads in file.Creates checksum of file line by line,
    Returns complete checksum total for file.
    """
    fp = open(path, 'rb')
    checksum = hashlib.md5()
    while True:
        buffer = fp.read(8192)
        if not buffer:
            break
        checksum.update(buffer)
    fp.close()
    checksum = checksum.hexdigest()
    return checksum