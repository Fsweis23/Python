import re
from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.party_model import Party

bcrypt = Bcrypt(app)

#Log in page
@app.route('/')
def index():
    return render_template('index.html')

#registration form processing
@app.route('/users/register', methods=['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/')
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hashed_pass
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/welcome')

#Login form processing
@app.route('/users/login', methods=['POST'])
def login():
    #see if the username/email provided exists in the database
    data = {'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    #if user is not regustered
    if not user_in_db:
        flash('Invalid login info', 'log')
        return redirect('/')
    #if the user exists, check the password!
    if not bcrypt.check_password_hash(user_in_db, request.form['password']):
        flash('Invalid login info', 'log')
    #log them in
    session['user_id'] = user_in_db.id
    return redirect('/welcome')

#Logout
@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')

#dashboard
@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    all_parties = Party.get_all()
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('dashboard.html', all_parties=all_parties, logged_user=logged_user)