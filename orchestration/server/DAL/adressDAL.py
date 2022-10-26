from pymongo import MongoClient

class AddressDAL:
    def __init__(self):
        self.__client=MongoClient("localhost", 27017)
        self.__db=self.__client["ex_python_addres"]
        self.__collection=self.__db["addres"]
    def get__collection(self):
        data=self.__collection.find({})
        return list(data)

