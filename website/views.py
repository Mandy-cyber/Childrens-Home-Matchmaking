from flask import Blueprint, jsonify, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .auth import login
from . import db 
import json

#TODO change html pages accordingly

#------------------------------------------------------------------------#
#GENERAL VIEWS
views = Blueprint('views', __name__)
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    print('')
    return render_template("home.html", user=current_user)

#------------------------------------------------------------------------#
#VIEWS TO DO WITH CHILDREN'S HOMES
@views.route('/chome', methods=['GET', 'POST'])
@login_required
def chome_profile():
    print('')
    return render_template("chome_profile.html", user=current_user)

@views.route('/chome-edit-profile', methods=['GET', 'POST'])
@login_required
def chome_edit_profile():
    print('')
    return render_template("chome_edit_your_profile.html", user=current_user)


#------------------------------------------------------------------------#
#VIEWS TO DO WITH DONATERS
@views.route('/donater', methods=['GET', 'POST'])
@login_required
def donater():
    print('')
    return render_template("d_profiles.html", user=current_user)
