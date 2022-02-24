
from app import app

from flask import render_template
from flask import flash

@app.route("/myviews")
def imho():
    flash("Sometimes I sit and think and sometimes I just sit ....")
    return render_template("public/myviews.html")

