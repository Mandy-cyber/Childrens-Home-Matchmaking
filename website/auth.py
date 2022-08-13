from flask import Blueprint, render_template, request, flash, redirect, url_for
# from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)
#TODO change names of html files 

#GET requests display content, POST requests submit content (sorta)
#------------------------------------------------------------------------#
#LOGIN as Donator

@auth.route('/login-donator', methods=['GET', 'POST']) #specifying which methods this page (view) will use
def login_donator():
    print("will fill this part in later")
    return render_template("login_donator.html") #display relevant html page


#------------------------------------------------------------------------#
#LOGIN as Children's Home

@auth.route('/login-chome', methods=['GET', 'POST'])
def login_chome():
    print("will fill this part in later")
    return render_template("login_chome.html")


#------------------------------------------------------------------------#
#LOGOUT

@auth.route('/logout')
@login_required #can only logout if you are already logged in 
def logout():
    logout_user() #logs out current user
    return redirect(url_for('views.home'))


#------------------------------------------------------------------------#
#SIGNUP as Donator

@auth.route('/sign-up-donator', methods=['GET', 'POST'])
def signup_donator():
    print("will fill this part in later")
    return render_template("signup_donator.html")


#------------------------------------------------------------------------#
#SIGNUP as Children's Home

@auth.route('/sign-up-chome', methods=['GET', 'POST'])
def signup_chome():
    print("will fill this part in later")
    return render_template("signup_chome.html")

#------------------------------------------------------------------------#