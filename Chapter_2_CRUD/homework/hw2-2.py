import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students
grades = db.grades

cursor = grades.find({'type': 'homework'}).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])

active_student = -1
for el in cursor:
    if active_student != el['student_id']:
        active_student = el['student_id']
        grades.remove(el)

