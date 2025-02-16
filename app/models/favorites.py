from app.extensions import db
from datetime import datetime

class Favorite(db.Document):
    user_id = db.ReferenceField('User', required=True)
    recipe_id = db.ReferenceField('Recipe', required=True)
    create_date = db.DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'favorites',
        'indexes': [{'fields': ['user_id', 'recipe_id'], 'unique': True}]
    }