# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 16:23:04 2015

@author: user
"""
from pprint import pprint

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    # 'students' here is the database name. It will be created if it does not exist.
    db = client.students
    return db
    
db = get_db()
dir(db)
collections = db.collection_names()

for i in db.grades.find():
    print pprint(i)
    