from flask import render_template, request, redirect, session, flash
from flask_app import app
# from flask_app.models.user import User

@app.route('/')
def index():
    return redirect("/users")

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/create', methods=['post'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')