from flask import Flask, render_template, redirect, jsonify, flash, send_file, session, request
from os import getenv
from database import *

from pdfGenerator import Generator

app = Flask("QR UNIMAG")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/download/qr")
def downloadQr():
    file = "static/img/qr.png"
    return send_file(file, as_attachment=True)

@app.route("/verify/<string:code>")
def verifyCode(code):
    
    qr = session.query(Codigo).filter(Codigo.id == code).first()

    condition = qr != None and qr.usado == 0
    
    if condition:
        qr.usado = 1

    response = "Válido" if condition else "No vaaaaaaa"


    return jsonify(response = str(response))

@app.route("/sendQr", methods=["POST"])
def generar():
    try:
        print(request.get_json())
        gen = Generator(int(request.get_json()["tickets"]))
        return jsonify(response = "success", message = "Código(s) envíados al destinatario")
    except:
        return jsonify(respose = "failed")


        
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True)