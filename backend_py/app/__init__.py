from flask import Flask, jsonify
from .config import get_config
from .models import db
from utils.sender import get_upload_dir
from flask_jwt_extended import JWTManager

# WARNING:
# FIX:
# TODO: Change this to relative path or change the frontend structure
path = get_upload_dir(levels_up=2, folder_name="frontend")
TEMPLATE_PATH = str(path)


def create_app():
    app = Flask(__name__, template_folder=TEMPLATE_PATH)  # name of the module
    app.config.from_object(get_config())

    #  Initialize extentions
    db.init_app(app)
    JWTManager(app)

    # register blueprints

    from .routes.auth_routes import auth_bp
    from .routes.ocr_routes import ocr_bp
    from .routes.default_routes import default_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(ocr_bp)
    app.register_blueprint(default_bp)

    # Create Table demo/dev
    with app.app_context():
        db.create_all()

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    return app
