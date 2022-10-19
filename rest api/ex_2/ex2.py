import json
import os
import sys
import requests

def get_user_by_id(id):
    url_users="https://jsonplaceholder.typicode.com/users"
    resp=requests.get(f"{url_users}/{id}")
    data =resp.json()
    if data["name"].startswith("E"):
        
        todos=requests.get(f"{url_users}/{id}/todos")
        data_todos =todos.json()
        with open(os.path.join(sys.path[0],"jfile.json"),"w")as f:
            json.dump(data_todos,f)
get_user_by_id(2)