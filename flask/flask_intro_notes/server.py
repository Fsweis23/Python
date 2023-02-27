from flask import Flask, render_template  # Import Flask to allow us to create our app
# import render_template to be able to serve html files
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'we can cahnge this!'  # Return the string 'Hello World!' as a response

@app.route('/or_this') #stack routes
@app.route('/success')
def success():
    return "success"

@app.route('/say/<word>/<int:number>')
# path variables go in <>
# be default path variables are strings
def say_word(word, number):
    # remember to bring your path variables in as parameters
    print(f"my word is {word}")
    print(number)
    return render_template("say.html", word=word, number=number)

@app.route("/template")
def template():
    new_variable = "This is a test string "
    return render_template("index.html", name_of_variable_on_template = new_variable)
    #                                    name_on_template = value_we_want

@app.route("/route_to_page_2")
def page2():
    return render_template("page2.html")

@app.route("/iterate")
def iterate():
    cats = [
        {
            'name': 'Garfield',
            'color': 'orange'
        },
        {
            'name': 'Scr',
            'color': 'dark brown'
        },
        {
            'name': 'Felix',
            'color': 'cat'
        },
    ]
    return render_template("cats.html", cats=cats, h=100, w=1000, color="pink")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.