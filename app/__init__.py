from config import db
from flask import Flask
from flask_migrate import Migrate

migrate = Migrate()


def create_app():
    application = Flask(__name__)

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)

    migrate.init_app(application, db)

    # 블루 프린트 등록
    from .routes.questions import question_blp
    from .routes.images import image_blp
    from .routes.choices import choices_blp
    from .routes.users import user_blp
    from .routes.answers import answer_blp
    
    application.register_blueprint(question_blp)
    application.register_blueprint(image_blp)
    application.register_blueprint(choices_blp)
    application.register_blueprint(user_blp)
    application.register_blueprint(answer_blp)
    
    if __name__ == "__main__":
        application.run(debug=True) 

    return application
