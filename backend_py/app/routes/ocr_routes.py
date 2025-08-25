from flask import Blueprint, jsonify, request, render_template
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename
from pathlib import Path
import grpc

from ..utils.validators import validate_file_type
from ..utils.errors import InvalidInputError
from ..utils.sender import send_to_ocr_service, get_upload_dir

ocr_bp = Blueprint("ocr", __name__, url_prefix="/ocr")


# TODO: Change this to a env variable or put it in config
ALLOWD_EXTENTION = {"jpg", "jpeg", "pdf"}


@ocr_bp.post("/upload")
# @jwt_required()
def upload():
    """
    This route lets users upload their record
    it accepts .jpg or .pdf
    """
    if "file" not in request.files:
        return jsonify({"err": "no file part in request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"err": "no selected file"}), 400

    if file and validate_file_type(file.filename, ALLOWD_EXTENTION):
        filename = secure_filename(file.filename)

        # TODO: add the functionality of what to do with the file
        path = get_upload_dir(levels_up=4) / f"{file.filename}"
        file.save(path)

        try:
            extracted_text = send_to_ocr_service(path)
            return jsonify({"extracted_text": extracted_text}), 200

        except grpc.RpcError as e:
            return jsonify({"error": f"grpc failed: {e.code()}"}), 500

        return jsonify({"msg": "File uploaded successfully", "filename": filename}), 200

    raise InvalidInputError("Invalid file Type")


@ocr_bp.get("/")
# @jwt_required()
def ocr():
    return render_template("ocr.html")
