from flask import Flask
app = Flask(__name__)
app.secret_key ="gotta cook em all"
DATABASE = 'recipes'