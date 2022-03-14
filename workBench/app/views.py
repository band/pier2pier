
from app import app

import flask
import subprocess

@app.route("/")
def index():
    return flask.render_template("public/index.html")

@app.route("/about")
def about():
    return flask.render_template("public/about.html")

@app.route("/command", methods=["GET", "POST"])
def your_command():
    p = {
        'args': ['awaiting your command ...'],
        'stdout': '(nothing)',
        'stderr': 'method is not POST'
    }
    if flask.request.method == "POST":
        cmd=[]
        cmd.append(flask.request.form["command"])
        p = subprocess.run(
            cmd,
            capture_output=True,
            encoding='UTF-8',
            shell=True
            )
        if p.returncode != 0:
            flask.flash("I'm sorry Dave, I'm afraid I can't do that.")

    return flask.render_template("public/your_command.html", p=p)
