from flask import Blueprint

recipe_bp = Blueprint('recipe', __name__, url_prefix='/recipe')

from app.blueprints.recipe import recipe
