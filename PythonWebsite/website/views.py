from flask import Blueprint , render_template
from flask.templating import _render

views = Blueprint('views', __name__)

@views.route('/')
#define the route, everything in the slash will run
def home():
    return render_template("home.html")

