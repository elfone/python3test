#!/usr/bin/env python3
"""
枚举sys.stdin.readline
"""
import sys
counter = 1
while True:
    line = sys.stdin.readline()
    if not line:
        break
    print("{}:{}".format(counter, line))
    counter += 1