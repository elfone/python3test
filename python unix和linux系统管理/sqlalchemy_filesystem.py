#!/usr/bin/env python3
__author__ = 'soarwilldo'
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData  # , ForeignKey
from sqlalchemy.orm import mapper, sessionmaker
import os

# path
path = '.'
# Part 1 :create engine
engine = create_engine('sqlite:///:memory:', echo=False)

# Part 2: metadata
metadata = MetaData()

filesystem_table = Table('filesystem', metadata,
                         Column('id', Integer, primary_key=True),
                         Column('path', String(500)),
                         Column('file', String(255)),
                         )

metadata.create_all(engine)


# part 3: mapped class
class Filesystem(object):
    def __init__(self, path, file):
        self.path = path
        self.file = file

    def __repr__(self):
        return '[Filesystem("%s", "%s")]' % (self.path, self.file)

# part 4: mapper function
mapper(Filesystem, filesystem_table)

# part 5: create session
# Session = sessionmaker(bind=engine, autoflush=True, transactional=True)
Session = sessionmaker(bind=engine, autoflush=True)
session = Session()

# part 6: crawl file system and populate database with results
for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        fullpath = os.path.join(dirpath, file)
        record = Filesystem(fullpath, file)
        # seesion.save(record)
        session.add(record)
        session.flush()

# part 7: commit to the database
session.commit()

# part 8: query
for record in session.query(Filesystem):
    print('Database Record Number: %s, Path: %s, File: %s'
          % (record.id, record.path, record.file))