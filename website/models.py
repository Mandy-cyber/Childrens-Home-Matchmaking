from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func


# class Donator(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(128))
#     last_name = db.Column(db.String(128))
#     donator_email = db.Column(db.String(256), unique=True)
#     donator_password = db.Column(db.String(16))

# class Home(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     home_name = db.Column(db.String(256), unique=True)
#     home_email = db.Column(db.String(256), unique=True)
#     home_password = db.Column(db.String(16))
#     home_location = db.Column(db.String(256))
#     home_population = db.Column(db.Integer)
#     home_specialization = db.Column(db.String(64))
#     home_description = db.Column(db.String(512))

# class Users(db.Model, UserMixin):

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(128))
    email = db.Column(db.String(256), unique=True)
    password = db.Column(db.String(16))
    urole = db.Column(db.String(20))
