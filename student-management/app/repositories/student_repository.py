from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.student_db
students_collection = db.students

class StudentRepository:
    @staticmethod
    def add_student(student):
        return students_collection.insert_one(student.to_dict())

    @staticmethod
    def get_students():
        return list(students_collection.find({}, {"_id": 0}))

    @staticmethod
    def get_student(email):
        return students_collection.find_one({"email": email}, {"_id": 0})

    @staticmethod
    def delete_student(email):
        return students_collection.delete_one({"email": email})
