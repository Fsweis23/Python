from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "dojo_survey"

@app.route('/')
def render_form():
    return render_template("index.html")

@app.route('/process_form', methods = ['POST'])
def process_form():
    print(request.form)
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favLocation'] = request.form['favLocation']
    session['comments'] = request.form['comments']
    return redirect("/show_info")

@app.route('show_info')
def show_info():
    name = request.form['name']
    dojo_location = request.form['dojo_location']
    favLanguage = request.form['favLanguage']
    comments = request.form['comments']
    return render_template("display.html", name = name, dojo_location = dojo_location, favLanguage = favLanguage, comments = comments)

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)