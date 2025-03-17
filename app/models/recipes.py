from app.extensions import mongo
from datetime import datetime

class Recipe:
    collection = mongo.db.recipes

    def __init__(self, recipe_data=None):
        if recipe_data:
            self.recipe_id = recipe_data.get('recipe_id')
            self.title = recipe_data.get('title')
            self.ingredients = recipe_data.get('ingredients', [])
            self.instructions = recipe_data.get('instructions', [])
            self.difficulty = recipe_data.get('difficulty')
            self.time = recipe_data.get('time')
            self.meal_type = recipe_data.get('meal_type')
            self.created_at = recipe_data.get('create_date')
            self.created_by = recipe_data.get('created_by')
        else:
            self.recipe_id = None
            self.title = None
            self.ingredients = []
            self.instructions = []
            self.difficulty = None
            self.time = None
            self.meal_type = None
            self.created_at = None

    @staticmethod
    def create_recipe(title:str, 
                     ingredients:list, 
                     instructions:list, 
                     difficulty:str,
                     time:str,
                     meal_type:str,
                     ) -> dict:

        recipe_data = {
            "title":        title,
            "ingredients":  ingredients,
            "instructions": instructions,
            "difficulty":   difficulty,
            "time":         time,
            "meal_type":    meal_type,
            "create_date":  datetime.utcnow(),
            "recipe_id":    Recipe.get_next_recipe_id(),
        }
        Recipe.collection.insert_one(recipe_data)
        return recipe_data

    @staticmethod
    def get_next_recipe_id() -> int:
        last_recipe = Recipe.collection.find_one(sort=[("recipe_id", -1)])
        return (last_recipe["recipe_id"] + 1) if last_recipe else 1
    
    @staticmethod
    def find_by_id(recipe_id: int):
        recipe_data = Recipe.collection.find_one({"recipe_id": int(recipe_id)})
        return Recipe(recipe_data) if recipe_data else None

    @staticmethod
    def delete_recipe(recipe_id:int):
        Recipe.collection.delete_one({"recipe_id": recipe_id})

    def to_dict(self):
        """Converte o objeto Recipe em um dicionário serializável"""
        return {
            'recipe_id': self.recipe_id,
            'title': self.title,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'difficulty': self.difficulty,
            'time': self.time,
            'meal_type': self.meal_type,
            'created_at': str(self.created_at) if self.created_at else None,
            'created_by': self.created_by
        }
