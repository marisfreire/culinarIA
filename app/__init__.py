# arquivo para inicialização de 'app' como módulo
import dotenv, os
from flask import Flask
from app.extensions import mongo
from flask_login import LoginManager

from app.blueprints.auth import auth_bp
from app.blueprints.menu import menu_bp
from app.blueprints.recipe import recipe_bp

from app.models.users import User

def create_app() -> Flask:
    app = Flask(__name__)

    dotenv.load_dotenv(dotenv.find_dotenv()) # carrega as variaveis de ambiente
    app.secret_key = os.getenv("SECRET_KEY")

    app.config["MONGO_URI"] = "mongodb://localhost:27017/culinaria"
    mongo.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(recipe_bp)

    return app