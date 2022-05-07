from flask import Blueprint, render_template, redirect, url_for

request = Blueprint("request", __name__)

@request.route("/login")
def login():
    return render_template("login.html")

@request.route("/sign-up")
def sign_up():
    return render_template("signup.html")    

@request.route("/logout")
def sign_up():
    return redirect(url_for("views.index"))     