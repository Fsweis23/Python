from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "counter_key"

@app.route('/')
def render_form():
    return render_template("index.html")

@app.route('/process_form', methods = ['POST'])
def process_form():
    print(request.form)
    session['add'] = request.form['reset']
    if not session['counter'] == "1" and not session['counter'] == '2':
        print("add 1")
        return redirect('/')

@app.route('show_info')
def show_info():
    if 'counter' in session:
        count = session['counter']
    return render_template("display.html", count = count)

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)