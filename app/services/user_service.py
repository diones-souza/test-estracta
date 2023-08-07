from app import db
from app.models.user import User
import bcrypt

def get_users():
    return User.query.all()

def create_user(data):
    password = bcrypt.hashpw(data.get('password').encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    user = User(username=data.get('username'), email=data.get('email'), password=password)
    
    db.session.add(user)
    db.session.commit()

    return user

def get_user(field, value):
    query = getattr(User, field, None)
    if query:
        return User.query.filter(query == value).first()
    return None

def update_user(user, data):
    if 'username' in data:
        user.username = data.get('username')

    if 'email' in data:
        user.email = data.get('email')

    if 'password' in data:
        user.password = data.get('password')

    db.session.commit()

    return user

def delete_user(user):
    db.session.delete(user)
    db.session.commit()
