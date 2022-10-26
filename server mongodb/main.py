from flask import Flask
import json
from bson import ObjectId

from routers.routerStudent import students

class JSONencoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


app=Flask(__name__)

app._json_encoder = JSONencoder

app.register_blueprint(students,url_prefix="/students")

app.run("localhost", 8000)