import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/Tesseract.exe'
import conexao

class Reconhece():
    def __init__(self):
        self.carro = conexao.CarroMorador()
    
    def reconheceCaracter(self):
        img_roi = cv2.imread("imgs/reconhecimento.jpg")
        config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'
        saida = pytesseract.image_to_string(img_roi, lang="eng", config=config)
        return saida

    def validaPlaca(self):
        placa = self.reconheceCaracter()
        placaC = placa[:7]
        result = self.carro.search(placaC)

        if (type(result) ==  str):
            return False
        else:
            if (result[0][1] == placaC):
                return True




