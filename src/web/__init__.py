from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Registrierung der Routen
    from src.web.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app