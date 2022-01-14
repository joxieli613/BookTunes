from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
#define the route, everything in the slash will run
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean = True)
@auth.route("/logout")
def logout():
    #pass value to the template by putting it as second arg in render template
    return render_template("home.html")
@auth.route("/sign-up")
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        if len(name) < 2:
            flash('Email must be longer')
        elif len(password < 8):
            pass
    return render_template("signup.html")
