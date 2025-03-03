from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt, jwt_required


def role_required(*roles):
    """
    Decorator to check if the user has one of the required roles.
    :param roles: One or more roles ('admin', 'renter') that are allowed to access the route.
    """

    def decorator(func):
        @wraps(func)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if claims.get('role') not in roles:
                return jsonify(
                    {"msg": f"Access denied: One of the following roles is required: {', '.join(roles)}"}), 403
                # return jsonify({"msg": f"Access denied: {required_role} role required"}), 403
            return func(*args, **kwargs)

        return wrapper

    return decorator
