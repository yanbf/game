from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.constant import DbConfig

app = Flask(__name__)
db_uri = DbConfig.get_db_uri()
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
print db_uri
db = SQLAlchemy(app)

from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Date,
    Float
)


class GamerTester(db.Model):
    __tablename__ = 'gamer_tester'

    id = db.Column('playerid', Integer, primary_key=True)
    name = db.Column('username', String(30), unique=True)
    email = db.Column('email', String(50), unique=True)
    password = db.Column('password', String(100), unique=False)

