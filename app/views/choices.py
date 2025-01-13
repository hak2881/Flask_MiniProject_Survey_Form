from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from ..models import Choices, db


choices_blp = Blueprint('Choices', 'choices', description="Operations on Choices", url_prefix='/choices')

# Choices 목록 조회

class ChoicesList(MethodView):
    @choices_blp.route('/',methods=["GET", "POST"])
    def get(self):
        choices = Choices.query.all()
        return jsonify([choice.to_dict() for choice in choices])

    @choices_blp.route('/edit',methods=["GET", "POST"])
    def post(self):
        data = request.json
        new_choice = Choices(
            content=data['content'],
            is_active=data['is_active'],
            sqe=data['sqe']
        )
        db.session.add(new_choice)
        db.session.commit()
        
        return jsonify({"msg": "Successfully created choice"}), 201

# 특정 Choice 조회, 수정, 삭제

class ChoiceResource(MethodView):
    @choices_blp.route('/<int:choice_id>',methods=["GET"])
    def get(self, choice_id):
        # 특정 Choice 조회
        choice = Choices.query.get_or_404(choice_id)
        return jsonify(choice.to_dict())
    
    @choices_blp.route('/edit/<int:choice_id>', methods =["PUT"])
    def put(self, choice_id):
        # 특정 Choice 수정
        choice = Choices.query.get_or_404(choice_id)
        data = request.json

        choice.content = data.get('content', choice.content)
        choice.is_active = data.get('is_active', choice.is_active)
        choice.sqe = data.get('sqe', choice.sqe)
        
        db.session.commit()
        return jsonify({'msg': 'Successfully updated choice'}), 200

    @choices_blp.route('/edit/<int:choice_id>',methods =["DELETE"])
    def delete(self, choice_id):
        # 특정 Choice 삭제
        choice = Choices.query.get_or_404(choice_id)
        db.session.delete(choice)
        db.session.commit()
        return jsonify({'msg': 'Successfully deleted choice'}), 200
