#!/usr/bin/env python3
__author__ = 'Administrator'


def calculatemd5(filename, block_size=2 ** 20):
    """Returns MD% checksum for given file."""
    import hashlib

    md5 = hashlib.md5()
    try:
        file = open(filename, 'rb')
        while True:
            data = file.read(block_size)
            if not data:
                break
            md5.update(data)
    except IOError:
        print('File \'' + filename + '\' not found!')
        return None
    except:
        return None
    return md5.hexdigest

