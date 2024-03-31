from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from database import *
import qrcode


class Generator():

    def __init__(self, qrs) -> None:
        width, height = letter
        cuadricule = canvas.Canvas("QRUNIMAG.pdf", pagesize=letter)

        salt = 1

        for i in range(1, qrs+1):
            cuadricule.rect(20, height - salt * 190, width-40, 180)
            cuadricule.drawImage(self.generateQr(), width-190, height- salt * 190, 170, 170)
            salt += 1

            if i % 4 == 0:
                cuadricule.showPage()
                salt = 1
        cuadricule.save()


    def generateQr(self):
        code = Codigo()
        session.add(code)
        session.commit()

        txt = f'{code.id}'
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=7, border=2)
        qr.add_data(txt)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        img.save(f"{code.id}.png")
        return f"{code.id}.png" 
