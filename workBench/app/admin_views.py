
from app import app

import flask

@app.route("/admin/dashboard")
def admin_dashboard():
    return flask.render_template("admin/dashboard.html")
