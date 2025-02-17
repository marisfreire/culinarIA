# arquivo para inicialização de 'app' como módulo
from flask import Flask
from app.extensions import db
from flask_login import LoginManager

from app.blueprints.auth import auth_bp
from app.blueprints.menu import menu_bp
from app.blueprints.recipe import recipe_bp

from app.models.users import User

def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(auth_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(recipe_bp)

    app.config["MONGODB_URI"] = "mongodb://localhost:27017/culinaria"
    
    mongo.init_app(app)
    
    import dotenv, os
    dotenv.load_dotenv(dotenv.find_dotenv()) # carrega as variaveis de ambiente
    app.secret_key = os.getenv("SECRET_KEY")

    return app