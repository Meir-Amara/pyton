from flask import Flask
from routers.userRouter import users

app=Flask(__name__)


app.register_blueprint(users,url_prefix="/users")

app.run("meir", 8000,debug=True)


