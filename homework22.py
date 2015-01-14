# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 16:23:04 2015

@author: user
"""

import pymongo
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
query = {'type':'homework'}
cursor = db.grades.find(query)
cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)])
sid = ""
count = 0
for item in cursor:
    pprint(item)
    count += 1
    print count
    while sid == "" or sid == item['student_id']:
        
    sid = item['student_id']