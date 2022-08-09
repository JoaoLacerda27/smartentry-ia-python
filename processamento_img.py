import os
import cv2
import imutils

def encontrar_contornos(img):
    conts = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    conts = imutils.grab_contours(conts)
    conts = sorted(conts, key=cv2.contourArea, reverse=True)[:8]
    return conts

def preProcessamentoPlaca(roi):
    if roi is None:
        return

    img_resize = cv2.resize(roi, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    frame_cinza = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)  # CINZA
    _, img_binary = cv2.threshold(frame_cinza, 170, 255, cv2.THRESH_BINARY)

    cv2.imwrite("imgs/reconhecimento.jpg", img_binary)

def preProcessamentoContornos(frame):
    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # CINZA
    blur = cv2.bilateralFilter(frame_cinza, 11, 17, 17)  # RUIDO
    edged = cv2.Canny(blur, 30, 200)  # linhas e contornos
    return edged

def apagaImagem():
    os.remove("imgs/reconhecimento.jpg")



