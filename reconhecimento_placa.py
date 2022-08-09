import cv2
import imutils

def reconhecePlaca():
    webcam = cv2.VideoCapture(0)
    if webcam.isOpened():
        validacao, frame = webcam.read()
        while validacao:
            validacao, frame = webcam.read()

            conts = encontrar_contornos(preProcessamentoContornos(frame))

            for c in conts:
                peri = cv2.arcLength(c, True)
                if peri > 120:
                    aprox = cv2.approxPolyDP(c, 0.03 * peri, True)
                    if len(aprox) == 4:
                        (x, y, alt, larg) = cv2.boundingRect(c)
                        cv2.rectangle(frame, (x, y), (x + alt, y + larg), (0, 255, 0), 2)
                        roi = frame[y + 3:(y + larg) - 3, x + 5:(x + alt) - 5]
                        preProcessamentoPlaca(roi)
                        break

            cv2.imshow("portão", frame)

            key = cv2.waitKey(50)
            if key == 27:
                break

    webcam.release()
    cv2.destroyAllWindows()

def encontrar_contornos(img):
    conts = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    conts = imutils.grab_contours(conts)
    conts = sorted(conts, key=cv2.contourArea, reverse=True)[:8]
    return conts

def preProcessamentoPlaca(roi):
    if roi is None:
        return

    img_resize = cv2.resize(roi, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

    frame_cinza = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)  # CINZA
    _, img_binary = cv2.threshold(frame_cinza, 170, 255, cv2.THRESH_BINARY)

    cv2.imwrite("imgs/reconhecimento.jpg", img_binary)

def preProcessamentoContornos(frame):
    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # CINZA
    blur = cv2.bilateralFilter(frame_cinza, 11, 17, 17)  # RUIDO
    edged = cv2.Canny(blur, 30, 200)  # linhas e contornos
    return edged



