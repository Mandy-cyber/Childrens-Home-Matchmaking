from flask import Blueprint, jsonify, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from . import db 
import json

#TODO change html pages accordingly

views = Blueprint('views', __name__)
@views.route('/', methods=['GET', 'POST'])
def home():
    print('put stuff here later')
    return render_template("home.html")

# @views.route('/signup', methods=['GET', 'POST'])
# def choose_a_signup():
#     print('put stuff here later')
#     return render_template("signup.html")