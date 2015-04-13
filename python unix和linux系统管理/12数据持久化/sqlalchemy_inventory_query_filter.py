#!/usr/bin/env python3
__author__ = 'Administrator'

from sqlalchemy_inventory_definition import session, OperatingSystem

for os in session.query(OperatingSystem).filter(OperatingSystem.name.like('Lin%')):
    print(os)