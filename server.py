from flask import Flask, render_template, redirect, jsonify, flash, send_file, session
from os import getenv
import random
import qrcode

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


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/generate/qr")
def generateQr():
    num = random.randint(0, 9999999)
    text = f"prueba{num}" 
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=7, border=2)
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save("static/img/qr.png")
    return redirect("/home")

@app.route("/download/qr")
def downloadQr():
    file = "static/img/qr.png"
    return send_file(file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)