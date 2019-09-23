from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blogs():
    return render_template("blogs.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(debug=True)