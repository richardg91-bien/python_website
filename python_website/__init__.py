
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt  import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY']='thisisfirstflaskapp'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/cjflask.db' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cjpostgres:yara25767@localhost:5432/python_websiteapp'

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] ='richardg91@gmail.com'
app.config['MAIL_PASSWORD'] = 'richard95778186'


mail=Mail(app)



from python_website import routes



