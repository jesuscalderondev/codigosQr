from flask import Flask, render_template, redirect, jsonify, flash
from os import getenv

app = Flask("QR UNIMAG")

app.config['MAIL_SERVER'] = getenv("MAIL_SERVER")
app.config['MAIL_PORT'] = getenv("MAIL_PORT")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SLS'] = False
app.config['MAIL_USERNAME'] = getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = getenv("MAIL_PASSWORD")

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)