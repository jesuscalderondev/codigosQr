from flask import Flask, render_template, redirect, jsonify, flash, send_file, session
from os import getenv
import random
import qrcode
from database import *

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
    code = Codigo()
    session.add(code)
    session.commit()

    txt = f'https://google.com/{code}'
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=7, border=2)
    qr.add_data(txt)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save("static/img/qr.png")
    return redirect("/home")

@app.route("/download/qr")
def downloadQr():
    file = "static/img/qr.png"
    return send_file(file, as_attachment=True)

@app.route("/verify/<string:code>")
def verifyCode(code):
    
    qr = session.query(Codigo).filter(Codigo.id.like(f'%{code}%')).first()

    condition = qr != None and qr.usado == 0
    
    if condition:
        qr.usado = 1

    response = "Válido" if condition else "No vaaaaaaa"


    return jsonify(response = str(response))
        
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True)