#!/usr/bin/env python3
__author__ = 'Administrator'
"""
至2015扌3月30日止，根据python3版的twisted官方文档暂时还不支持twisted。spread模块，
因此本段代码无法执行，仅作记录。
"""

from twisted.spread import pb
from twisted.internet import reactor


class RBDirLister(pb.Root):
    def remote_ls(self, directory):
        try:
            return os.listdir(directory)
        except OSError:
            return []

    def remote_ls_boom(self, directory):
        return os.listdir(directory)

if __name__ == '__main__':
    reactor.listenTCP(9876, pb.PBServerFactory(PBDirLister()))
    reactor.run()