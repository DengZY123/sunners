# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from flask_sqlalchemy import SQLAlchemy
from application import db




class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100))
    mobile = db.Column(db.String(11))
    avatar = db.Column(db.String(255))
    status = db.Column(db.Integer)
    updated_time = db.Column(db.DateTime)
    created_time = db.Column(db.DateTime)
