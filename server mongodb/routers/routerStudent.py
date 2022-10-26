from flask import Blueprint, jsonify, request
from BLL.BLLstudents import StudentsBLL

students_bll=StudentsBLL()

students = Blueprint("students", __name__)

@students.route("/", methods=["GET"])
def get_all_students():
    students = students_bll.get_all_students()
    return jsonify(students)

@students.route("/", methods=["POST"])
def add_student():
    obj=request.json
    students = students_bll.add_student(obj)
    return jsonify(students)
@students.route("/<string:id>", methods=["DELETE"])
def delete_student(id):
    
    students = students_bll.delete_student(id)
    return jsonify(students)

