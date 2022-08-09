import asyncio
import cv2
import processamento_img as pi
import reconhecimento_caracter as rc

def reconhecePlaca():
    reconhece_caracter = rc.Reconhece()
    webcam = cv2.VideoCapture(0)
    if webcam.isOpened():
        validacao, frame = webcam.read()
        while validacao:
            validacao, frame = webcam.read()
            conts = pi.encontrar_contornos(pi.preProcessamentoContornos(frame))

            for c in conts:
                peri = cv2.arcLength(c, True)
                if peri > 120:
                    aprox = cv2.approxPolyDP(c, 0.03 * peri, True)
                    if len(aprox) == 4:
                        (x, y, alt, larg) = cv2.boundingRect(c)
                        cv2.rectangle(frame, (x, y), (x + alt, y + larg), (0, 255, 0), 2)
                        roi = frame[y + 3:(y + larg) - 3, x + 5:(x + alt) - 5]
                        pi.preProcessamentoPlaca(roi)
                        if (reconhece_caracter.validaPlaca()):
                            print("SINAL ABRE PORTÃO")
                            # await asyncio.sleep(0.5)
                        else:
                            print("SINAL NÃO ABRE PORTÃO")
                            # await asyncio.sleep(0.2)

            cv2.imshow("SmartEntry", frame)

            key = cv2.waitKey(50)
            if key == 27:
                break

    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    reconhecePlaca()