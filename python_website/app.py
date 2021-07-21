
from flask import app
from flask import url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow  import Marshmallow
from python_website.forms import RegistrationForm, LoginForm
from python_website.models import User 




app.config['SECRET_KEY']='123456'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)


     