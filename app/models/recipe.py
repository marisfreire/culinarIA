from app.extensions import db
from datetime import datetime

class Recipe(db.Document):
    title = db.StringField(required=True)
    ingredients = db.ListField(db.StringField(), required=True)
    instructions = db.ListField(db.StringField(), required=True)
    create_date = db.DateTimeField(default=datetime.utcnow)
    user_id = db.ReferenceField('User', required=True)
    tags = db.ListField(db.StringField())
    
    meta = {
        'collection': 'recipes',
        'ordering': ['create_date']
    }
