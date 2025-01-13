from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from ..models import Answer, db

answer_blp = Blueprint('Answer', 'answer', url_prefix='/answer')

@answer_blp.route('/')
class AnswerList(MethodView):
    def get(self):
        answers = Answer.query.all()  
        return jsonify([answer.to_dict() for answer in answers]), 201
    
@answer_blp.route('/edit')
class AnswerCreate(MethodView):
    def post(self):
        data = request.json
        new_answer = Answer(choice_id=data["choice_id"], user_id=data["user_id"])
        db.session.add(new_answer)
        db.session.commit()
        return jsonify({"msg": "Created Answer"}), 201
    
@answer_blp.route('/<int:user_id>/<int:choice_id>')
class AnswerGet(MethodView):
    def get(self,user_id, choice_id):
        answers = Answer.query.filter_by(user_id=user_id, choice_id=choice_id).all()
        if not answers:
            return {"msg":"No Found Data"}
        return [answer.to_dict() for answer in answers]

@answer_blp.route('/edit/<int:user_id>/<int:choice_id>')
class PostAnswer(MethodView):
    def post(self,user_id, choice_id):
        new_answer = Answer(user_id=user_id, choice_id=choice_id)
        db.session.add(new_answer)
        db.session.commit()
        return new_answer.to_dict()