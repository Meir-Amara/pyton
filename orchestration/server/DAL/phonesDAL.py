import sys
import os
import json

class PhonsDAL:
    def __init__(self):
        self.__path=os.path.join(sys.path[0], "data\phons.json")
    def get_phons(self):
        with open(self.__path,'r') as f:
            data=json.load(f)
        return list(data)
