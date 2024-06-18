from shop.settings import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(20), nullable = False)
    password_confirmation = db.Column(db.String(20), nullable = False)

    is_admin = db.Column(db.Boolean)
    
    def __repr__(self) -> str:
        return f"Ім'я користувача - {self.name}"
