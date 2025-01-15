from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from ..models import Image, db

image_blp = Blueprint("image", "image", description="Operations On Image", url_prefix="/image")

# 이미지 생성
@image_blp.route('/')
class ImageCreate(MethodView):
    def post(self):
        data = request.json
        if not data or 'url' not in data or 'type' not in data:
            return jsonify({"msg": "Invalid data"}), 400

        new_img = Image(
            url=data['url'],
            type=data['type']
        )
        db.session.add(new_img)
        db.session.commit()

        return jsonify({"msg": f"ID: {new_img.id} Image Success Create"}), 201
    def get(self):
        imgs = Image.query.all()
        return jsonify([img.to_dict() for img in imgs]), 200


@image_blp.route('/admin/<int:image_id>')
class ImageModify(MethodView):

    def put(self, image_id):
        # 특정 이미지 수정
        img = Image.query.get_or_404(image_id)
        data = request.json

        img.url = data.get('url', img.url)  # URL 수정, 없으면 기존 값 유지
        img.type = data.get('type', img.type)  # Type 수정, 없으면 기존 값 유지

        db.session.commit()
        return jsonify({"msg": "Successfully updated Img"}), 200

    def delete(self, image_id):
        # 특정 이미지 삭제
        img = Image.query.get_or_404(image_id)

        db.session.delete(img)
        db.session.commit()
        return jsonify({"msg": "Successfully deleted Img"}), 200

@image_blp.route("/main")
class ImageMain(MethodView):
    def get(self):
        main_img = Image.query.filter_by(type="main").first()

        if main_img is None:
            return jsonify({"msg":"No main image found"}), 404

        return jsonify({"image":main_img.url}), 200

