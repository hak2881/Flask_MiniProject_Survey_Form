from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from config import db
from models import User

user_blp = Blueprint("Users", "users", description="Operations on users", url_prefix="/users")

@user_blp.route("/")
class User(MethodView):
    def get(self):
        users = User.query.all()
        return jsonify(users)

def post():
    user_data = request.json
    new_user = User(
        name = user_data['name'],
        age = user_data['age'],
        gender = user_data['gender'],
        email = user_data['email']
        )
    db.session.add(new_user)
    db.session.commit()

@user_blp.route('/<int:user_id>')
class Users(MethodView):
    def get(self,user_id):
        user = User.query.get_or_404(user_id)
        return {"name": user.name, 'email': user.email}
    
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        user_data = request.json

        user.name = user_data['name']
        user.email = user_data['email']
        user.gender = user_data['gender']
        user.age = user_data['age']

        db.session.commit()
        return {"message": "User updated"}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}