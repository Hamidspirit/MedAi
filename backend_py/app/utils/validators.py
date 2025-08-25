from ..utils.errors import InvalidInputError


def require_json_keys(data: dict, keys: list[str]):
    """"""
    missing = [k for k in keys if k not in data]
    if missing:
        raise InvalidInputError(f"Missing required fields: {
                                ', '.join(missing)}")


def validate_username(username: str):
    """"""
    if not username or len(username) < 3:
        raise InvalidInputError("Username should be longer than 3 charachters")


def validate_password(password: str):
    """"""
    if not password or len(password) < 5:
        raise InvalidInputError("Password should be longer than 5 character")


def validate_file_type(filename: str, allowd: set):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowd
