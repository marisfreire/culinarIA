from app.extensions import mongo
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin):
    collection = mongo.db.users

    def __init__(self, user_data=None):
        if user_data:
            self.id = user_data['user_id']
            self.email = user_data['email']
            self.name = user_data['name']
            self.favorites_recipes_id = user_data.get('favorites_recipes_id', [])
            self.recipes_favorited = user_data.get('recipes_favorited', 0)
            self.preferences = user_data.get('preferences', {
                'dietary_restrictions': [],
                'skill_level': 'iniciante'
            })
        else:
            self.id = None
            self.email = None
            self.name = None
            self.favorites_recipes_id = []
            self.recipes_favorited = 0
            self.preferences = {
                'dietary_restrictions': [],
                'skill_level': 'iniciante'
            }

    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(user_id):
        user_data = User.collection.find_one({"user_id": int(user_id)})
        if user_data:
            user = User(user_data)
            return user
        return None

    @staticmethod
    def get_next_user_id() -> int:
        last_user = User.collection.find_one(sort=[("user_id", -1)])
        return (last_user["user_id"] + 1) if last_user else 1

    @staticmethod
    def create_user(email:str, 
                    password:str, 
                    name="", 
                    dietary_restrictions = [], 
                    skill_level = "iniciante"
                    ) -> dict:

        user_data = {
            "user_id":       User.get_next_user_id(),
            "email":         email,
            "password_hash": generate_password_hash(password),
            "name":          name,
            "create_date":   datetime.utcnow(),
            "preferences": {
                "dietary_restrictions": dietary_restrictions, # ex: gluten free, vegano, intolerante a lactose
                "skill_level": skill_level # iniciante, intermediário, avançado 
            },
            "recipes_favorited": 0,
            "favorites_recipes_id": []
        }
        User.collection.insert_one(user_data)
        return user_data

    @staticmethod
    def find_by_email(email:str):
        return User.collection.find_one({"email": email})

    @staticmethod
    def check_password(user:str, password:str):
        return check_password_hash(user["password_hash"], password)

    @staticmethod
    def increment_recipes_favorited(user_id:int):
        User.collection.update_one(
            {"user_id": user_id},
            {"$inc": {"recipes_favorited": 1}}
        )

    @staticmethod
    def decrement_recipes_favorited(user_id:int):
        User.collection.update_one(
            {"user_id": user_id, "recipes_favorited": {"$gt": 0}},
            {"$inc": {"recipes_favorited": -1}}
        )

    def add_favorite_recipe(self, recipe_id:int):
        if recipe_id not in self.favorites_recipes_id:
            User.collection.update_one(
                {"user_id": self.id},
                {"$addToSet": {"favorites_recipes_id": recipe_id}}
            )
            self.favorites_recipes_id.append(recipe_id)
            self.increment_recipes_favorited(self.id)

    def remove_favorite_recipe(self, recipe_id:int):
        if recipe_id in self.favorites_recipes_id:
            User.collection.update_one(
                {"user_id": self.id},
                {"$pull": {"favorites_recipes_id": recipe_id}}
            )
            self.favorites_recipes_id.remove(recipe_id)
            self.decrement_recipes_favorited(self.id)

    def get_favorite_recipes(self) -> list:
        from app.models import Recipe
        favorite_recipes = []
        for recipe_id in self.favorites_recipes_id:
            recipe = Recipe.find_by_id(recipe_id)
            if recipe:
                favorite_recipes.append(recipe)
        return favorite_recipes