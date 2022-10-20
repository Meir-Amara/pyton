from flask import Flask, jsonify, request

app = Flask(__name__)

cars = [{"id": 1, "model": "Mazda", "year": 2001, "colors": [
         "red", "blue"], "driver":{"first_name": "meir", "last_name": "amara"}},
        {"id": 2, "model": "BMW", "year": 2020, "colors": [
        "black", "white"], "driver":{"first_name": "eden", "last_name": "amara"}}]

@app.route("/cars", methods=["GET"])
def get_all_cars():
    return jsonify(cars)

@app.route("/cars/<int:id>", methods=["GET"])
def get_car(id):
    li = list(filter(lambda car: car["id"] == id, cars))
    return jsonify(li[0])

@app.route("/cars", methods=["POST"])
def create_car():
    data = request.json
    cars.append(data)
    return jsonify(cars)

@app.route("/cars/<string:id>", methods=["PUT"])
def update_car(id):
    data = request.json
    for car in cars:
        if car["id"] == int(id):
            car["model"] = data["model"]
            break
    return jsonify(cars)

@app.route("/cars/<string:id>", methods=["DELETE"]) 
def delete_car(id):
    index = -1
    for i in range(len(cars)):
        if cars[i]["id"] == int(id):
            index = i
            break
    cars.pop(index)
    return jsonify(cars)

app.run()