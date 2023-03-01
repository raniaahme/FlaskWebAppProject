# pip install flask-sqlalchemy
from mypackage import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(student_id):
	return Student.query.get(int(student_id))


class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_image = db.Column(db.String(120))
    subjects = db.relationship('Subject', backref='editor', lazy=True)
    
def __repr__(self):
		return f"Student('{self.username}', '{self.password}')"

    
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text)
    duration = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    
def __repr__(self):
		return f"Post('{self.name}', '{self.duration}')"
    