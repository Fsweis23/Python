from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.sports_model import Sports

@app.route("/sports/new")
def new_sports_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("sports_new.html")

@app.route("/sports/create", methods=['POST'])
def process_sports():
    if 'user_id' not in session:
        return redirect('/')
    if not Sports.validator(request.form):
        return redirect('/sports/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    id = Sports.create(data)
    return redirect('/welcome')

@app.route("/sports/<int:id>/delete")
def del_sports(id):
    if 'user_id' not in session:
        return redirect('/')
    sport = Sports.get_by_id({'id':id})
    if not int(session['user_id']) == sport.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    sport.delete({'id':id})
    return redirect('/welcome')

@app.route("/sports/<int:id>/edit")
def edit_sport_form(id):
    if 'user_id' not in session:
        return redirect('/')
    sport = Sports.get_by_id({'id':id})
    if not int(session['user_id']) == sport.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    sport = Sports.get_by_id({'id':id})
    return render_template("sports_edit.html", sport = sport)

@app.route("/sports/<int:id>/update", methods=['POST'])
def update_sport(id):
    if 'user_id' not in session:
        return redirect('/')
    sport = Sports.get_by_id({'id':id})
    if int(session['user_id']) != sport.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    if not Sports.validator(request.form):
        return redirect(f"/sports/{id}/edit")
    data = {
        **request.form,
        'id':id,
        'user_id':session['user_id']
    }
    Sports.update(data)
    return redirect('/welcome')

@app.route("/sports/<int:id>")
def show_sport(id):
    sport = Sports.get_by_id({'id':id})
    return render_template("sports_one.html", sport = sport)

@app.route("/my_sports")
def my_sports():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_by_id({'id':session['user_id']})
    return render_template("my_sports.html", logged_user = user)