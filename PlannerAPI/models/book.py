from flask_sqlalchemy import SQLAlchemy
from app.extensions import db

class Book(db.Model):
    __tablename__ = 'books'
    __table_args__ = {"schema": "plannerapp_dev"}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('plannerapp_dev.users.id'))

    def __repr__(self):
        return '' % self.title % self.description % self.year % self.author_id