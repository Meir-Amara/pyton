import requests

class PersonDAL:
    def __init__(self):
        self.__url="https://jsonplaceholder.typicode.com/users"
    def get_persons(self):
        resp=requests.get(self.__url)
        data=resp.json()
        return list(data)


        