from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    roll_no = db.Column(db.String(50), unique=True, nullable=False)
    student_class = db.Column(db.String(50), nullable=False)
    marks = db.Column(db.Integer, nullable=False)
    attendance = db.Column(db.Float, nullable=False)
    contact = db.Column(db.String(100), nullable=False)

class ChatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(500))
    response = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime)
