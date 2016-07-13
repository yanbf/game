from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

def init_db():
    db.create_all()

def flush():
    db.session.commit()

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
