from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def initial_render():
    return "http://localhost:5000/playground"

@app.route("/playground")
def container():
    return render_template('index.html')

@app.route("/playground/<square_count>")
def other_container(container_count):
    others = int(container_count)
    return render_template('index2.html', others = others)

@app.route("/playground/<box_count>/<other_color>")
def container_color(container_count, multiple_colors):
    others = (int(container_count))
    multipleColors = multiple_colors
    return render_template('index3.html', others = others, multipleColors = multipleColors )

if __name__ == "__main__":
    app.run(debug = True)