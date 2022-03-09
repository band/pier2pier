
import flask

app = flask.Flask(__name__)

app.config["SECRET_KEY"] = "016hOdMleWZ4uJjt2CG0NmA"

from app import views
from app import admin_views
from app import myviews
