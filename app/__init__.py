from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True  # Modo debug para desarrollo

    # Importar y registrar las rutas
    from .routes import api_bp
    from .auth import auth_bp
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

