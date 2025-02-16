# arquivo para inicialização de 'app' como módulo
'''from flask import Flask

app = Flask(__name__)

from app.blueprints.home.routes import home'''

from flask import Flask
from app.config import Config
from app.extensions import db
from flask_login import LoginManager

from app.routes.auth import auth_bp
from app.routes.menu import menu_bp
from app.routes.recipe import recipe_bp
from app.routes.routes import main_bp

from app.models.users import User

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    
    db.init_app(app)