from app.extensions import mongo
from datetime import datetime

class Recipe:
    collection = mongo.db.recipes

    @staticmethod
    def create_recipe(title:str, 
                      ingredients:list[str], 
                      instructions:list[str], 
                      user_id:int, 
                      tags=None
                      ) -> dict:

        recipe_data = {
            "title":        title,
            "ingredients":  ingredients,
            "instructions": instructions,
            "create_date":  datetime.utcnow(),
            "user_id":      user_id,
            "tags":         tags if tags else []
        }
        Recipe.collection.insert_one(recipe_data)
        return recipe_data

    @staticmethod
    def find_by_user(user_id:int):
        return list(Recipe.collection.find({"user_id": user_id}).sort("create_date", 1))

    @staticmethod
    def find_by_title(title:str):
        return list(Recipe.collection.find({"title": {"$regex": f"^{title}$", "$options": "i"}}))

    @staticmethod
    def find_by_tag(tag):
        return list(Recipe.collection.find({"tags": tag}))

    @staticmethod
    def delete_recipe(recipe_id:int):
        Recipe.collection.delete_one({"_id": recipe_id})
