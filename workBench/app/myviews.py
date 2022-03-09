
from app import app

import flask

@app.route("/myviews")
def imho():
    flask.flash("Sometimes I sit and think and sometimes I just sit ....")
    return flask.render_template("public/myviews.html")

