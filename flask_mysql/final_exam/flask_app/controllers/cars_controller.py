from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.cars_model import Cars

@app.route("/cars/new")
def new_cars_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("cars_new.html")

@app.route("/cars/create", methods=['POST'])
def process_cars():
    if 'user_id' not in session:
        return redirect('/')
    if not Cars.validator(request.form):
        return redirect('/cars/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    id = Cars.create(data)
    return redirect('/welcome')

@app.route("/cars/<int:id>/cancel")
def del_cars(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Cars.get_by_id({'id':id})
    if not int(session['user_id']) == car.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    car.delete({'id':id})
    return redirect('/welcome')

@app.route("/cars/<int:id>/edit")
def edit_car_form(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Cars.get_by_id({'id':id})
    if not int(session['user_id']) == car.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    car = Cars.get_by_id({'id':id})
    return render_template("cars_edit.html", car = car)

@app.route("/cars/<int:id>/update", methods=['POST'])
def update_car(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Cars.get_by_id({'id':id})
    if int(session['user_id']) != car.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    if not Cars.validator(request.form):
        return redirect(f"/cars/{id}/edit")
    data = {
        **request.form,
        'id':id,
        'user_id':session['user_id']
    }
    Cars.update(data)
    return redirect('/welcome')

@app.route("/cars/<int:id>")
def show_car(id):
    car = Cars.get_by_id({'id':id})
    return render_template("cars_one.html", car = car)

@app.route("/my_cars")
def my_cars():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_by_id({'id':session['user_id']})
    return render_template("my_cars.html", logged_user = user)