#!/usr/bin/env python3
__author__ = 'Administrator'
"""
至2015扌3月30日止，根据python3版的twisted官方文档暂时还不支持twisted。spread模块，
因此本段代码无法执行，仅作记录。
"""

from twisted.spread import pb
from twisted.internet import reactor

def handle_err(reason):
    print("an error occurred", reason)
    reactor.stop()

def call_ls(def_call_obj):
    return def_call_obj.callRemote('ls_boom', '/home/jmjones/logs')

def print_ls(print_result):
    print(print_result)
    reactor.stop()

if __name__ == '__main__':
    factory =pb.PBClientFactory()
    reactor.connectTCP('localhost', 9876, factory)
    d = factory.getRootObject()
    d.addCallback(call_ls)
    d.addCAllback(print_ls)
    d.addErrback(handle_err)
    reactor.run()