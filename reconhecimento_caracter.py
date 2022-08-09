import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/Tesseract.exe'
import conexao

class Reconhece():
    def __init__(self):
        self.carro = conexao.Carro()
    
    def reconheceCaracter(self):
        img_roi = cv2.imread("imgs/reconhecimento.jpg")
        config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'
        saida = pytesseract.image_to_string(img_roi, lang="eng", config=config)
        return saida

    def validaPlaca(self):
        placa = self.reconheceCaracter()
        placaC = placa[:7]
        result = self.carro.search(placaC)
        # result = self.carro.search('BRA2E19')

        if (type(result) ==  str):
            # print("TUPLA =" + result)
            # print("PLACA =" + placa)
            print("NÃO ABRE")
            return False
        else:
            if (result[0][1] == placaC):
                # print("TUPLA" + result[0][1])
                # print("PLACA" + placaC)
                print("ABRE PORTÃO")
            return True




