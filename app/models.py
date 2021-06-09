from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from sqlalchemy import UniqueConstraint




class Users(db.Model):
    __tablename__ = 'users_db'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200),nullable=False)
    address = db.Column(db.String(200),nullable=False)
    phone = db.Column(db.String(200),nullable=False)
    mobile_phone = db.Column(db.String(200))
    email = db.Column(db.String(200))
    UniqueConstraint('name', name='name_unique')
