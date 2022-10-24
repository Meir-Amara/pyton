import json
import sys
import os


class Person :
    def __init__(self):
        self.__path=os.path.join(sys.path[0], "data/persons.json")
    def get_all_movies(self):
        with open(self.__path,"r")as f:
            data=json.load(f)
            return data 
    def delete_persons(self,id):
        pers=self.get_all_movies()
        for per in pers: 
            if per["id"]==id:
                per
dicts = [
     { "name": "Tom", "age": 10 },
     { "name": "Mark", "age": 5 },
     { "name": "Pam", "age": 7 },
     { "name": "Dick", "age": 12 }
 ]

x=next(item for item in dicts if item["name"] == "Pam")
print(x)



