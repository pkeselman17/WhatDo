from flask_sqlalchemy import SQLAlchemy
from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {"schema": "plannerapp_dev"}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    books = db.relationship('Book', backref='author')

    def __init__(self, username, email):
      self.username = username
      self.email = email

    def __repr__(self):
        return '' % self.id