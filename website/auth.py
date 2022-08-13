#GET requests display content, POST requests submit content (sorta)
from flask import Blueprint, render_template, request, flash, redirect, url_for
# from .models import User
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from functools import wraps

auth = Blueprint('auth', __name__)

#------------------------------------------------------------------------#
#TESTING SOMETHING HERE
def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return login_manager.unauthorized()
            if ((current_user.urole != role) and (role != "ANY")):
                return login_manager.unauthorized()      
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
# https://stackoverflow.com/questions/15871391/implementing-flask-login-with-multiple-user-classes



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
@login_required(role="ANY")
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