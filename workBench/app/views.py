
from app import app

from flask import render_template, request, redirect
from flask import flash

import subprocess

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/command", methods=["GET", "POST"])
def your_command():
    p = {
        'stdout': '(nothing)',
        'stderr': 'method is not POST'
    }
    if request.method == "POST":
        cmd = request.form["command"]
        p = subprocess.run(
            cmd.split(),
            capture_output=True,
            encoding='UTF-8',
            shell=True
            )
        if p.returncode != 0:
            flash("I'm sorry Dave, I'm afraid I can't do that.")

    return render_template("public/your_command.html", p=p)
