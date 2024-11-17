import jwt
import datetime
from flask import Blueprint, jsonify, request
from functools import wraps

auth_bp = Blueprint('auth', __name__)
SECRET_KEY = "super_secret_key"  # Cambia esto a algo seguro

# Usuarios simulados
users = {
    "admin": "password123",
    "user1": "mypassword"
}

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Endpoint para autenticarse y obtener un token JWT.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username] == password:
        # Crear token
        token = jwt.encode({
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expira en 1 hora
        }, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token}), 200
    return jsonify({"error": "Credenciales inválidas"}), 401

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Token no proporcionado"}), 401
        try:
            token = token.split(" ")[1]  # Formato: Bearer <token>
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401
        return f(*args, **kwargs)
    return wrapper