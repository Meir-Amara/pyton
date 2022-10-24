from flask import Blueprint,jsonify
from BLL.BLL_movies import Movies

movies_bll=Movies()

movies=Blueprint("movies",__name__)

@movies.route('/',methods=["GET"])
def get_all_movies():
    movies=movies_bll.get_all_movies()
    return list(map(lambda obj:{"name":obj["name"],"rating":obj["rating"]["average"]},movies))