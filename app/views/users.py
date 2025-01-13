from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from ..models import User

user_blp = Blueprint("Users", "users", description="Operations on users", url_prefix="/users")

class UserList(MethodView):
    @user_blp.route("/", methods=["GET"])
    def get(self):
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

    @user_blp.route("/", methods=["POST"])
    def post(self):
        user_data = request.json
        new_user = User(
            name=user_data['name'],
            age=user_data['age'],
            gender=user_data['gender'],
            email=user_data['email'],
            is_admin=user_data['is_admin']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 201


class UserResource(MethodView):
    @user_blp.route('/<int:user_id>', methods=["GET"])
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict()), 200
    
    @user_blp.route('/<int:user_id>', methods=["PUT"])
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        user_data = request.json

        user.name = user_data.get('name', user.name)
        user.email = user_data.get('email', user.email)
        user.gender = user_data.get('gender', user.gender)
        user.age = user_data.get('age', user.age)
        user.is_admin = user_data.get('is_admin', user.is_admin)

        db.session.commit()
        return jsonify({"msg": "User updated successfully"}), 200

    @user_blp.route('/<int:user_id>', methods=["DELETE"])
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"msg": "User deleted successfully"}), 200
