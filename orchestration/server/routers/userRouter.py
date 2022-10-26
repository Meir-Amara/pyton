from flask import Blueprint, jsonify
from BLL.uersBLL import UsersBLL

users_BLL=UsersBLL()

users=Blueprint("x",__name__)

@users.route("/", methods=["GET"])
def get_all_users():
    users=users_BLL.get_users()
    return jsonify(users)