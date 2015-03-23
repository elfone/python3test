#!/usr/bin/env python3
"""
使用enumerate函数将枚举sys.stdin.readline写得非常短小
"""
__author__ = 'Administrator'

import sys
for i, line in enumerate(sys.stdin):
    print('{}:{}'.format(i, line))