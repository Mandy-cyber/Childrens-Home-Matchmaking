from flask import Blueprint, jsonify, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from . import db 
import json

#TODO change html pages accordingly

views = Blueprint('views', __name__)
@views.route('/', methods=['GET', 'POST'])
def home():
    print('')
    return render_template("home.html")

@views.route('/chome', methods=['GET', 'POST'])
def chome_profile():
    print('')
    return render_template("chome_profile.html")

@views.route('/donater', methods=['GET', 'POST'])
def donater():
    print('')
    return render_template("d_profiles.html")
