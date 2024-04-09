from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import inch
#from rotatedText import verticalText
from database import *
import qrcode


class Generator():

    def __init__(self, qrs) -> None:
        width, height = A4
        cuadricule = canvas.Canvas("archivo.pdf", pagesize=letter)

        for i in range(1, qrs+1):
            code = self.generateQr()
            num = generateNum(code[1])

            cuadricule.drawImage("Plantilla.png", x=0, y=0, width=width+15, height=height-30)
            cuadricule.drawImage(code[0], x=width/4 + 7.5, y = height/6 - 10, width=width/2, height=height/3.2)

            cuadricule.setFont("Helvetica-Bold", 40)
            cuadricule.drawString(x=40, y= height-100,text=num, charSpace=1)

            print(num)
            cuadricule.showPage()

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

        img.save(f"qrs/{code.id}.png")
        return f"qrs/{code.id}.png", code.boleto
    
def generateNum(num:int):
    numTxt = str(num)
    return (4-len(numTxt)) * "0" + numTxt 

