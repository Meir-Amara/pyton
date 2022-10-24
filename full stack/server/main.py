from flask import Flask
from routers.ruoterMovies import movies

app=Flask(__name__)

app.register_blueprint(movies, url_prefix="/movies")
app.register_blueprint(persons, url_prefix="/persons")


app.run("localhost", 8000)
