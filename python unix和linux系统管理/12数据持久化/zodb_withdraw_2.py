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

while True:
    try:
        transaction.begin()
        noah.withdraw(300)
        jeremy.deposit(300)
        transaction.commit()
    except custom_class_zodb.OutOfFunds:
        print('OutOfFunds Error')
        print('Current account information:')
        print(noah)
        print(jeremy)
        transaction.abort()
        break

print('AFTER WITHDAWAL')
print('===============')
print(noah)
print(jeremy)
print('----------------')

conn.close
