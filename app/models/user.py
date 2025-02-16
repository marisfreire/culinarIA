from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Document):
    user_id = db.IntField(unique=True, required=True) # falta colocar a lógica para criar o id 
    email = db.EmailField(required=True, unique=True)
    username = db.StringField(required=True, unique=True, max_length=50)
    password_hash = db.StringField(required=True)
    name = db.StringField(max_length=100)
    
    create_date = db.DateTimeField(default=datetime.utcnow)
    
    preferences = db.DictField(default={
        'dietary_restrictions': [],  # ex: ['vegetariano', 'gluten-free']
        'favorite_cuisines': [],    # ex: ['italiano', 'japonês']
        'skill_level': 'iniciante'   # iniciante, intermediario, avançado
    })
    
    recipes_created = db.IntField(default=0)
    recipes_favorited = db.IntField(default=0)
    
    meta = {
        'collection': 'users',
        'indexes': ['email', {'fields': ['create_date'], 'expireAfterSeconds': -1}]
    }
    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def increment_recipes_created(self):
        self.recipes_created += 1
        self.save()
        
    def increment_recipes_favorited(self):
        self.recipes_favorited += 1
        self.save()
        
    def decrement_recipes_favorited(self):
        if self.recipes_favorited > 0:
            self.recipes_favorited -= 1
            self.save()


    @classmethod # método para busca
    def find_by_email(cls, email):
        return cls.objects(email=email).first()
