#!/usr/bin/env python3
__author__ = 'Administrator'

from sqlalchemy_inventory_definition import session, OperatingSystem

ubuntu_710 = OperatingSystem(name='linux', description='2.6.22-14 kernel')
#session.save(ubuntu_710)
session.add(ubuntu_710)
session.flush()
session.commit()