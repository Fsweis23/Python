from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.shows_model import Shows

@app.route("/shows/new")
def new_shows_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("shows_new.html")

@app.route("/shows/create", methods=['POST'])
def process_shows():
    if 'user_id' not in session:
        return redirect('/')
    if not Shows.validator(request.form):
        return redirect('/shows/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    id = Shows.create(data)
    return redirect('/welcome')

@app.route("/shows/<int:id>/delete")
def del_shows(id):
    if 'user_id' not in session:
        return redirect('/')
    show = Shows.get_by_id({'id':id})
    if not int(session['user_id']) == show.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    show.delete({'id':id})
    return redirect('/welcome')

@app.route("/shows/<int:id>/edit")
def edit_show_form(id):
    if 'user_id' not in session:
        return redirect('/')
    show = Shows.get_by_id({'id':id})
    if not int(session['user_id']) == show.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    show = Shows.get_by_id({'id':id})
    return render_template("shows_edit.html", show = show)

@app.route("/shows/<int:id>/update", methods=['POST'])
def update_show(id):
    if 'user_id' not in session:
        return redirect('/')
    show = Shows.get_by_id({'id':id})
    if int(session['user_id']) != show.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    if not Shows.validator(request.form):
        return redirect(f"/shows/{id}/edit")
    data = {
        **request.form,
        'id':id,
        'user_id':session['user_id']
    }
    Shows.update(data)
    return redirect('/welcome')

@app.route("/shows/<int:id>")
def show_show(id):
    show = Shows.get_by_id({'id':id})
    return render_template("shows_one.html", show = show)

@app.route("/my_shows")
def my_shows():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_by_id({'id':session['user_id']})
    return render_template("my_shows.html", logged_user = user)