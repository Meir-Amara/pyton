import requests

resp=requests.get("http://127.0.0.1:5000/cars")
data =resp.json()

colors=input("enter colors car")

list_colors=colors.split()

car={"id": len(data)+1, "model": input("enter the model car"), "year": int(input("enter year car")), "colors":list_colors
    , "driver":{"first_name":  input("enter the first name"), "last_name": input("enter the last name")}}

requests.post("http://127.0.0.1:5000/cars",json=car)
