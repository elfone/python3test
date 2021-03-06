#!/usr/bin/env python3
__author__ = 'Administrator'
import ZODB
import ZODB.FileStorage

filestorage = ZODB.FileStorage.FileStorage('zodb_filestorage.db')
db = ZODB.DB(filestorage)
conn = db.open()

root = conn.root()
print(root.items())

conn.close()