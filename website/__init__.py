from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'changethislater' #encrypting session data
    app.config['SQLALCHEMY_DATABSE_URI'] = f"sqlite:///{DB_NAME}" #location of database
    db.init_app(app)
    return app

def create_database(app):
    #if the database does not already exist (specifically in the website folder) then create it
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("database created successfully")