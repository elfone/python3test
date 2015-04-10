#!/usr/bin/env python3
__author__ = 'Administrator'
import ZODB
import ZODB.FileStorage
import transaction
import custom_class_zodb

filestorage = ZODB.FileStorage.FileStorage('zodb_filestorage.db')
db = ZODB.DB(filestorage)
conn = db.open()

root = conn.root()
noah = root['noah']

print('BEFORE WITHDRAL')
print('===============')
print(noah)

jeremy = root['jeremy']
print(jeremy)
print('---------------')

transaction.begin()
noah.withdraw(300)
jeremy.deposit(300)
transaction.commit()

print('AFTER WITHDAWAL')
print('===============')
print(noah)
print(jeremy)
print('----------------')

conn.close
