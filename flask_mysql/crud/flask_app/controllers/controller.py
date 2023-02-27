from flask import render_template
from flask_app import app
from flask_app.models.crud_model import CR

@app.route('/')
def index():
    return render_template('index.html')