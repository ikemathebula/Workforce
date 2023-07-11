from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db, app
from flask_login import UserMixin


'''create a user model'''
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    user_created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'user_id': self.user_id, 'Username': self.username,
            'Email': self.email, 'password': self.password,
            'user_created_at': self.user_created_at
        }
    
    def get_id(self):
        return str(self.user_id)
    

    with app.app_context():
        db.create_all()