from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:56465646@localhost/portfolio'
app.config['SQLALCHEMY_DATABASE_TRACK_MODIFICATIONS'] = False
app.config['FLASK_DEBUG'] = True
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_POOL_SIZE'] = 10
app.config['SQLALCHEMY_POOL_RECYCLE'] = 500


'''create an instance of SQLAlchemy database'''
db = SQLAlchemy(app)
