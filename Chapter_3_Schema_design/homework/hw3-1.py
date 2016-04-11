import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
students = db.students

cursor = students.find()


for student in cursor:
    print student['_id']
    scores = student['scores']
    min_homework = (-1, 100)
    for i,el in enumerate(scores):
        if el['type'] == 'homework':
            if el['score'] < min_homework[1]:
                min_homework = (i, el['score'])
    del scores[min_homework[0]]
    res = students.update_one({"_id": student["_id"]}, {"$set": {"scores": scores}})
    print res.__dict__
