import dotenv, os
from flask import Flask
from app.extensions import mongo, login_manager


def create_app() -> Flask:
    app = Flask(__name__, 
                template_folder='src',
                static_folder='src')

    dotenv.load_dotenv(dotenv.find_dotenv()) # carrega as variaveis de ambiente
    app.secret_key = os.getenv("SECRET_KEY")
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    
    print(f"Mongo object: {mongo}") # para debugar
    if(mongo.cx):
        
        print("MongoDB connection established")
    else:
        print("Failed do connect to MongoDB")

    mongo.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    from app.models.users import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    from app.blueprints.auth import auth_bp
    from app.blueprints.menu import menu_bp
    from app.blueprints.recipe import recipe_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(recipe_bp)

    return app