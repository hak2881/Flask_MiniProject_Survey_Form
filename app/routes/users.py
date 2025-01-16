from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from ..models import User , db

user_blp = Blueprint("Users", "users", description="Operations on users", url_prefix="/signup")

@user_blp.route('/')
class UserCreate(MethodView):
    def post(self):
        user_data = request.json
        new_user = User(
            name=user_data['name'],
            age=user_data['age'],
            gender=user_data['gender'],
            email=user_data['email']
        )
        existing_user = User.query.filter_by(email=new_user.email).first()
        if existing_user:
            return jsonify({"ValueError": "이미 존재하는 계정 입니다."}), 409
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": f"{new_user.name}님 회원가입을 축하합니다",
                        "user_id": new_user.id}), 201

    def get(self):
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])


@user_blp.route('/<int:user_id>')
class UserResource(MethodView):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict()), 200

@user_blp.route('/admin/<int:user_id>')
class UserModify(MethodView):
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        user_data = request.json

        user.name = user_data.get('name', user.name)
        user.email = user_data.get('email', user.email)
        user.gender = user_data.get('gender', user.gender)
        user.age = user_data.get('age', user.age)

        db.session.commit()
        return jsonify({"msg": "User updated successfully"}), 200


    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"msg": "User deleted successfully"}), 200

