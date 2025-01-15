from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from ..models import Choices, db


choices_blp = Blueprint('Choices', 'choices', description="Operations on Choices", url_prefix='/choice')

# Choices 목록 조회

@choices_blp.route('/')
class ChoicesCreate(MethodView):
    def post(self):
        data = request.json
        new_choice = Choices(
            content=data['content'],
            is_active=data['is_active'],
            sqe=data['sqe'],
            question_id=data['question_id']
        )
        db.session.add(new_choice)
        db.session.commit()
        
        return jsonify({"msg": f"Content: {new_choice.content} choice Success Create"}), 201
    
        def get(self):
            choices = Choices.query.all()
            return jsonify([choice.to_dict() for choice in choices])

# 특정 Choice 조회, 수정, 삭제
@choices_blp.route('/<int:question_id>')
class ChoiceResource(MethodView):

    def get(self, question_id):
        # 특정 Choice 조회
        choices = Choices.query.filter_by(question_id=question_id).all()
        return {"choices":[{"id":choice.id,"content":choice.content,"is_active":choice.is_active,"sqe":choice.sqe}for choice in choices]}
    
@choices_blp.route('/admin/<int:choice_id>')
class ChoiceModify(MethodView):
    def put(self, choice_id):
        # 특정 Choice 수정
        choice = Choices.query.get_or_404(choice_id)
        data = request.json

        choice.content = data.get('content', choice.content)
        choice.is_active = data.get('is_active', choice.is_active)
        choice.sqe = data.get('sqe', choice.sqe)
        
        db.session.commit()
        return jsonify({'msg': 'Successfully updated choice'}), 200


    def delete(self, choice_id):
        # 특정 Choice 삭제
        choice = Choices.query.get_or_404(choice_id)
        db.session.delete(choice)
        db.session.commit()
        return jsonify({'msg': 'Successfully deleted choice'}), 200
