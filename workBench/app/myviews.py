
from app import app

from flask import render_template

@app.route("/public/myviews")
def imho():
    return render_template("public/myviews.html")

