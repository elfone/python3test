#!/usr/bin/env python3
__author__ = 'Administrator'
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto.rfc1902 import ObjectName
# 暂时无法使用，但可以执行，仅作记录用。因为找不到windows下的net-snmp所以这里用pysnmp代替原代码中的netsnmp


class Snmp(object):
    """A basic SNMP session"""

    def __init__(self,
                 oid='sysDescr',
                 Version=2,
                 DesHost='localhost',
                 Community='public'):
        # if oid == 'sysDescr':
        #     oid = '1.3.6.1.2.1.1.1'
        self.oid = oid
        self.version = Version
        self.desHost = DesHost
        self.community = Community

    def query(self):
        """Creates SNMP query session"""
        try:
            if self.version == 2:
                mpModel = 1
            elif self.version == 1:
                mpModel = 0
            else:
                print('err snmp Version {}'.format(self.version))
                result = None
                return result

            errorIndication, errorStatus, errorIndex, result = \
                cmdgen.CommandGenerator().getCmd(
                    cmdgen.CommunityData('my-agent', self.community, mpModel),
                    cmdgen.Udp6TransportTarget((self.desHost, 161)),
                    cmdgen.MibVariable('SNMPv2-MIB', self.oid).loadMibs(),
                    lookupNames=True,
                    lookupValues=True
                    # ObjectName(self.oid)
                    # self.oid
                )
        except Exception as err:
            print(err)
            result = None

        return result