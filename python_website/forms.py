from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import validators
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegistrationForm(FlaskForm):
    username = StringField(label= 'Username', validators=[DataRequired(), Length(min=3, max=20)] )
    email = StringField(label='Email', validators=[DataRequired(), Length
    (min=3, max=30)])
    password = StringField(label= 'Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField(label='<confirm Password', validators={DataRequired(), EqualTo('password')}) 
    submit = SubmitField(label='Sign Up', validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Length
    (min=3, max=30)])
    password = StringField(label= 'Password', validators=[DataRequired(), Length(min=6, max=25)])
    submit = SubmitField(label='Login', validators=[DataRequired()])
    
class ResetPasswordForm(FlaskForm):
    password = StringField(label= 'Password', validators=[DataRequired(), Length(min=6, max=25)])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('Confirm Password')]) 
    submit = SubmitField(label='Change Password', validators=[DataRequired()])


class ResetRequestForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Length
        (min=3, max=30)])
    submit = SubmitField(label='Reset Password')

class AccountUpdateForm(FlaskForm):
    firstname= StringField(label= 'Firstname', validators=[DataRequired(), Length(min=3, max=20)] )
    lastname= StringField(label= 'Lastname', validators=[DataRequired(), Length(min=3, max=20)] )
    username = StringField(label= 'Username', validators=[DataRequired(), Length(min=3, max=20)] )
    email = StringField(label='Email', validators=[DataRequired(), Length
    (min=3, max=30)])
    picture=FileField(label="Update Profile Picture", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField(label='Update Account')