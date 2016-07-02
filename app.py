from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql://root:lf721521@ec2-54-200-98-228.us-west-2.compute.amazonaws.com"


@app.route('/hello_word/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'The about page'
