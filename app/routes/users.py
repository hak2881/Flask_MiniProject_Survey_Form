from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from ..models import User , db

user_blp = Blueprint("Users", "users", description="Operations on users", url_prefix="/users")

@user_blp.route('/')
class UserList(MethodView):
    
    def get(self):
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

@user_blp.route('/edit')
class UserCreate(MethodView):
    def post(self):
        user_data = request.json
        new_user = User(
            name=user_data['name'],
            age=user_data['age'],
            gender=user_data['gender'],
            email=user_data['email'],
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 201

@user_blp.route('/<int:user_id>')
class UserResource(MethodView):
    
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict()), 200
    
@user_blp.route('/edit/<int:user_id>')
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
