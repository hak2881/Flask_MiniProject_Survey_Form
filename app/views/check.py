from flask import request, jsonify
from ..models import User

def check_admin(name):
    user = User.query.filter_by(name= name)
    if not user :
        return False
    if not user:
        return False  # 사용자가 없다면 False 반환
    
    return True