from pydoc import doc
from pymongo import MongoClient
from bson import objectid
import requests

client = MongoClient("localhost", 27017)
db = client["moviesxdb"]
collection = db["movie"]

url ="https://api.tvmaze.com/shows" 

res=requests.get(url)
data=res.json()
data=data[:10]

data=list(map(lambda obj:{"name":obj["name"],"genres":obj["genres"],"average_runtime":obj["averageRuntime"]},data))

# Create a new document


# collection.insert_many(data)


def change_movie_name():
    mongo_data=list(collection.find({}))
    movie_name=input("the name u want to change")
    names_movies=map(lambda obj:obj["name"],mongo_data)
    print(movie_name)
    if movie_name in list(names_movies):
        new_name_movie=input("the new name u want")
        doc={"name":new_name_movie}
        collection.update_one({"name": movie_name}, {"$set": doc})

# names_movies=map(lambda obj:obj["name"],data)


change_movie_name( )