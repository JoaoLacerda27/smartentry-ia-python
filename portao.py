import sys

from pymata4 import pymata4
import time

class Portao:
    def __init__(self):
        self.pin = 7
        self.i = 0
        self.board = pymata4.Pymata4()
        self.board.set_pin_mode_servo(self.pin)

    def rotateServo(self, angle):
        self.board.servo_write(self.pin, angle)
        time.sleep(0.003)


    def abrePortao(self):
        try:
            for i in range(self.i, 180):
                self.rotateServo(i)

        except KeyboardInterrupt:
            self.board.shutdown()
            sys.exit(0)

    def fechaPortao(self):
        try:
            for i in range(180, 1, -1):
                self.rotateServo(i)

        except KeyboardInterrupt:
            self.board.shutdown()
            sys.exit(0)

if __name__ == '__main__':
    portao = Portao()
    portao.abrePortao()
    time.sleep(2)
    portao.fechaPortao()

