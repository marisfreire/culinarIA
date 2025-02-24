from flask_pymongo import PyMongo
from flask_login import LoginManager

mongo = PyMongo()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from app.models.users import User
    user_data = User.collection.find_one({"user_id": int(user_id)})
    if user_data:
        user = User()
        user.id = user_data["user_id"]
        return user
    return None
