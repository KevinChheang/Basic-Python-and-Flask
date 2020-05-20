from flask import Flask, request

app = Flask(__name__)


@app.route("/welcome")
def welcome_page():
    return "welcome"


@app.route("/welcome/home")
def home_page():
    return "welcome home"


@app.route("/welcome/back")
def back_page():
    return "welcome back"
