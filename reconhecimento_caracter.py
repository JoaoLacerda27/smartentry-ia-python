import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/Tesseract.exe'
import crud as db

class Reconhece():
    def reconheceCaracter(self):
        img_roi = cv2.imread("imgs/reconhecimento.jpg")
        config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'
        saida = pytesseract.image_to_string(img_roi, lang="eng", config=config)
        return saida

    def validaPlaca(self):
        if (db.Carro().search(self.reconheceCaracter(), type_s="placa") == True):
            print("ABRE PORTÃO")
            return True
        else:
            print("NÃO ABRE")
            return False
