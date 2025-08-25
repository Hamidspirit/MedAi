from flask import jsonify


class ApiError(Exception):
    status_code = 400
    error = "Bad Request"

    def __init__(self, message="Bad Request", status_code=None):
        super().__init__(message)
        if status_code is not None:
            self.status_code = status_code
        self.message = message

    def to_response(self):
        response = jsonify({"error": self.message})
        response.status_code = self.status_code
        return response


class InvalidInputError(ApiError):
    status_code = 400


class UnauthorizedError(ApiError):
    status_code = 401


class ConflictError(ApiError):
    status_code = 409
