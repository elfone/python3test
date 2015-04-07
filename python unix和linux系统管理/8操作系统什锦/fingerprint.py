#!/usr/bin/env python3
__author__ = 'Administrator'
import platform

"""
Fingerporints the following Operating systems:
* Mac OS X
* Ubuntu
* Red Hat/Cent OS
* FreeBSD
* SunOS
* Windows
"""


class OpSysType(object):
    """Determins OS Type using platform module"""

    def __getattr__(self, item):
        if item == 'osx':
            return 'osx'
        elif item == 'rhel':
            return 'redhst'
        elif item == 'ubu':
            return 'ubuntu'
        elif item == 'fbsd':
            return "FreeBSD"
        elif item == 'sun':
            return 'SunOS'
        elif item == 'win':
            return 'Windows'
        elif item == 'unknown_linux':
            return 'unknown_linux'
        elif item == 'unknown':
            return 'unknown'
        else:
            raise AttributeError(item)

    def linuxType(self):
        """Uses various methods to determine Linux Type"""

        if platform.dist() == self.rhel:
            return self.rhel
        elif platform.uname()[1] == self.ubu:
            return self.ubu
        elif platform.uname()[0] == self.Windows:
            return self.Windows
        else:
            return self.unknown_linux

    def winType(self):
        """Uses various methods to determine Windows Type"""
        return platform.platform()

    def queryOS(self):
        if platform.system() == 'Darwin':
            return self.osx
        elif platform.system() == 'Linux':
            return self.linuxType()
        elif platform.system() == self.sun:
            return self.sun
        elif platform.system() == self.fbsd:
            return self.fbsd
        elif platform.system() == 'Windows':
            return self.winType()


def fingerprint():
    type = OpSysType()
    print(type.queryOS())


if __name__ == '__main__':
    fingerprint()