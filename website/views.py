from flask import Blueprint, jsonify, render_template, flash, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .auth import login
from . import db 
from .models import User, Home, Donater
import json

#TODO change html pages accordingly

#------------------------------------------------------------------------#
#GENERAL VIEWS
views = Blueprint('views', __name__)
@views.route('/', methods=['GET', 'POST'])
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
    if request.method == 'POST':
        home_name = request.form.get('home_name')
        current_email = request.form.get('current_email')
        home_email = request.form.get('home_email')
        home_location = request.form.get('home_location')
        home_population = request.form.get('home_population')
        home_specialization = request.form.get('home_specialization')
        home_description = request.form.get('home_description')
        #---------------------------#
        #Updating User Table
        this_user = User.query.filter_by(email=current_email).first() 
        if len(home_name) > 0:
            this_user.full_name = home_name
            db.session.commit()
        else:
            print('')
        if len(home_email) > 0:
            this_user.email = home_email
            db.session.commit()
        else:
            print('')
        #---------------------------#
        #Updating Home Table
        home = Home.query.filter_by(home_email=current_email).first() 
        if home:
            home.home_name = this_user.full_name
            home.home_email = this_user.email
            db.session.commit()
            if len(home_location) > 0:
                home.home_location = home_location
                db.session.commit()
            else:
                print('No change')
            if len(home_population) > 0:
                home.home_population = home_population
                db.session.commit()
            else:
                print('No change')
            if len(home_specialization) > 0:
                home.home_specialization = home_specialization
                db.session.commit()
            else:
                print('No change')
            if len(home_description) > 0:
                home.home_description = home_description
                db.session.commit()
            else:
                print('No change')
        else:
            home_name = this_user.full_name
            home_email = this_user.email
            if len(home_location) > 0:
                home_location = home_location
            else:
                home_location = " "
            if len(home_population) > 0:
                home_population = home_population
            else:
                home.home_population = " "
            if len(home_specialization) > 0:
                home_specialization = home_specialization
            else:
                home_specialization = " "
            if len(home_description) > 0:
                home_description = home_description
            else:
                home_description = ""
            new_home = Home(home_name=home_name, home_email=home_email, home_location=home_location, home_population=home_population, home_specialization=home_specialization, home_description=home_description)
            db.session.add(new_home)
            db.session.commit()
        db.session.commit()

        print(home.home_name, home.home_email, home.home_location, home.home_population, home.home_specialization, home.home_description)
        return redirect(url_for('views.chome_profile'))
    return render_template("chome_edit_your_profile.html", user=current_user)


#------------------------------------------------------------------------#
#VIEWS TO DO WITH DONATERS
@views.route('/donater', methods=['GET', 'POST'])
@login_required
def donater():
    print('')
    return render_template("d_profiles.html", user=current_user)


@views.route('/matchmaking-survey', methods=['GET', 'POST'])
@login_required
def donater_edit_profile():
    if current_user.urole != "Donater":
        return redirect(url_for("views.home"))
    if request.method == 'POST':
        print('')
    else: 
        return render_template("match.html", user=current_user)