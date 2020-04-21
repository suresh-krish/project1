import os
from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from models import User,db


app = Flask(__name__)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key="email"

db.init_app(app)
def main():
    db.create_all()

# Check for environment variable


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if (request.method == "POST"):
        mail = request.form['name']
        passw = request.form['pwd']

        # count = User.query.filter_by(email=mail).count()
        # print (count)
        try:
            register = User(email = mail, password = passw)
            db.session.add(register)
            db.session.commit()
            a=User.query.all()
            print(a)
            return render_template("register.html",name=mail)
        except:
            error="You have already registered with this email"
            return render_template("register.html",message=error)
    return render_template("register.html")

@app.route("/login.html",methods=["GET","POST"])
def login():
    return render_template("login.html")
