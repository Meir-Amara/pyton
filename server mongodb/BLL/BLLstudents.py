from pymongo import MongoClient
from bson import ObjectId

class StudentsBLL:
    def __init__(self):
        self.__client=MongoClient("localhost", 27017)
        self.__db=self.__client["studentsDBpy"]
        self.__collection=self.__db["student"]
    def get_all_students(self):
        data=self.__collection.find({})
        return list(data)

    def get_student_by_id(self,id):
        data=self.__collection.find_one({"_id":ObjectId(id)})
        return list(data)
    
    def get_student_by_name(self,name):
        data=self.__collection.find_one({"firstName":name})
        return list(data)
    
    def add_student(self,obj):
        self.__collection.insert_one(obj)
        data=self.__collection.find({})
        return list(data)
    
    def update_student(self,obj,id):
        self.__collection.update_one({"_id":ObjectId(id)},{"$set":obj})
        data=self.__collection.find({})
        return list(data)
    
    def delete_student(self,id):
        self.__collection.delete_one({"_id":ObjectId(id)})
        data=self.__collection.find({})
        return list(data)