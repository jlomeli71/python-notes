from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mywebsite():
    return render_template("index.html")

@app.route("/work.html")
def about():
    return render_template("work.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return "These are my thoughs in blogs ..."

