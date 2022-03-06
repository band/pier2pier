
from app import app

from flask import render_template, request, redirect
from flask import flash

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/command", methods=["GET", "POST"])
def your_command():
    if request.method == "POST":
        command = request.form["command"]
        flash("Sorry, I can't do that, Dave ....")
        return redirect(request.url)

    return render_template("public/your_command.html")
