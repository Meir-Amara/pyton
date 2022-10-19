import requests

url="https://jsonplaceholder.typicode.com/users"


# all
resp=requests.get(url)
data =resp.json()

for user in data:
    print(user["name"])

# by id
resp=requests.get(f"{url}/2")
data =resp.json()
print(data)


# add new user
obj={"name":"meir","age":22}
resp=requests.post(url,obj)
data =resp.json()
print(data)

# update user
obj={"name":"meir","age":22}
resp=requests.patch(f"{url}/7",obj)
data =resp.json()
print(data)

# delete user 
resp=requests.delete(f"{url}/5")
data =resp.json()
print(data)

