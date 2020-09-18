import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")  # 127.0.0.1:5000
def index():
    return render_template("homepage.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/login")
def login():
    return render_template("login.html")


# dynamic route
@app.route("/<location>")
def business(location):
    return render_template("business.html", location=location)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
