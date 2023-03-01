from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from mypackage.model import Student, Subject

class RegistrationForm(FlaskForm):
	username = StringField(
		'Username',
		validators=[
			DataRequired(),
			Length(min=3, max=20)
		]
	)
	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email()
		]
	)
	password = PasswordField(
		'Password',
		validators=[
			DataRequired()
		]
	)
	confirm_password = PasswordField(
		'Confirm Password',
		validators=[
			DataRequired(),
			EqualTo('password')
		]
	)
	name = StringField(
		'Name',
		validators=[
			DataRequired(),
			Length(min=3, max=20)
		]
	)
	age = IntegerField(
			'Age',
			validators=[
				DataRequired()
			]
		)
	submit = SubmitField(
		'Sign Up'
	)


	# custom validation for duplicates
	def validate_username(self, username):
		student = Student.query.filter_by(username=username.data).first()
		if student:
			raise ValidationError('Username already exists')

	def validate_email(self, email):
		student = Student.query.filter_by(email=email.data).first()
		if student:
			raise ValidationError('Email already exists')


class LoginForm(FlaskForm):
	username  = StringField(
		'Username',
		validators=[
			DataRequired(),
			Length(min=3, max=20)
		]
	)
	password = PasswordField(
		'Password',
		validators=[
			DataRequired()
		]
	)
	submit = SubmitField(
		'Sign In'
	)
 
 
class SubjectForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[
                    DataRequired(),
                    Length(min=3, max=20)
                   ]
    )
    content = TextAreaField(
        'Content',
        validators=[
                    DataRequired(),
                   ]
    )
    duration = IntegerField(
        'Duration',
        validators=[
                    DataRequired(),
                   ]
    )
    student_id = IntegerField(
		'Student ID',
        validators=[
                    DataRequired()
                   ],
        # render_kw={'readonly':True}
	)
    submit = SubmitField(
        'Submit',
    ) 