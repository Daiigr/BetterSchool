from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
print(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@host/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(100), nullable=False)
       email = db.Column(db.String(100), nullable=False, unique=True)
       # Add additional fields as needed

class Lesson(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       title = db.Column(db.String(100), nullable=False)
       content = db.Column(db.Text, nullable=False)
       # Add additional fields as needed

       