# RUN THIS FILE WITH python test.py read_users
from mypackage import db,app
import sys
from mypackage.model import Student, Subject

# create database
def create_db():
	with app.app_context():
		# you will have instance folder with site.db inside
		db.create_all()

# -------------------------- CRUD OPERATIONS --------------------------
# Create operation
def create_student():
	with app.app_context():
		student = Student(name='rania',age='22',username='rania25', email='rania1121999@gmail.com', password='123')
		db.session.add(student)
		db.session.commit()
  
# Read operation
def read_student():
    with app.app_context():
        print(Student.query.all())
        
# Update operation
def update_student():
	with app.app_context():
		student = Student.query.filter_by(username="rania25").first()
		student.username = 'rania25'
		db.session.commit()
  		# print(student)
    
# Delete operation
def delete_student():
    with app.app_context():
        student = Student.query.filter_by(username='rania25').first()
        db.session.delete(student)
        db.session.commit()
        
             
# Create operation
def create_subject():
	with app.app_context():
		student = Student.query.first()
		student1 = Subject(id=1, name='Python', content='Python',duration=54, student_id=student.id)
		student2 = Subject(id=2, name='php', content='php', duration=20,student_id=student.id)
		db.session.add(student1)
		db.session.add(student2)
		db.session.commit()

# Read operation
def read_student_subject():
    with app.app_context():
        student = Student.query.first()
        print(student.subjects)
        
# Read operation       
def read_subject():
    with app.app_context():
        subject = Subject.query.first()
        print(subject)
        print(subject.student_id)
        
        
# snippet to allow us to run funcs from terminal with "python test.py print_func"
if __name__ == '__main__':
	globals()[sys.argv[1]]()