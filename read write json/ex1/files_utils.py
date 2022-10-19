import json
import sys
import os

path = os.path.join(sys.path[0], "person.json")

with open(path,'r') as f:
    data=json.load(f)

print(data)
def get_data_by_address(an):
    for per in data:
        # print(per)
        if per["Address"]["Street"]["Name"]==an:
            print(per["Name"])
            print(per["Address"]["City"])
            print(per["Address"]["Street"]["Name"],per["Address"]["Street"]["Number"])

get_data_by_address('jerusalem street')