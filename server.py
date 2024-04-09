from flask import Flask, render_template, redirect, jsonify, flash, send_file, session, request
from os import getenv
from database import *
from datetime import timedelta, datetime
from flask_mail import Mail
from mailManager import sendMessage
from dotenv import load_dotenv

from pdfGeneratorCh import Generator

app = Flask("QR UNIMAG")

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SLS'] = False
app.config['MAIL_USERNAME'] = getenv('USER_MAIL')
app.config['MAIL_PASSWORD'] = getenv('MAIL_PASSWORD')
mail = Mail()

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

@app.route("/sendQr", methods=["POST"])
def generar():
    try:
        data = request.get_json()
        Generator(int(data["tickets"]))
        #sendMessage(mail, data['email'], data['fullname'])
        return jsonify(response = "success", message = "Código(s) envíados al destinatario")
    except Exception as e:
        print(e)
        return jsonify(respose = "failed", message = "No lo envía")

@app.route("/verify/<string:qr>")
def verifyQr(qr):
    code = session.get(Codigo, qr)

    if code != None and code.usado == False:
        code.usado = True
        session.add(code)
        session.commit()

        return f"Boleto #{code.boleto} válido"
    return "Este boleto no es válido para el ingreso"


@app.route("/copy/database")
def copyDatabase():
    return send_file("database.db")

        
if __name__ == "__main__":
    load_dotenv()
    Base.metadata.create_all(engine)
    mail.init_app(app)
    app.run(debug=True, host="0.0.0.0", port=5000, load_dotenv=True)