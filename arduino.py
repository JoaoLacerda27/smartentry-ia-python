import sys
from pymata4 import pymata4
import time

class Config():
    def __init__(self):
        self.pin = 7
        self.triggerPin = 11
        self.echoPin = 12
        self.board = pymata4.Pymata4()
        self.board.set_pin_mode_servo(self.pin)
        self.board.set_pin_mode_sonar(self.triggerPin, self.echoPin, self.the_callback)
        self.i = 0
        self.distance = 0

class Arduino(Config):
    def __init__(self):
        Config.__init__(self)

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
        if(self.capturaSensor()):
            try:
                for i in range(180, 1, -1):
                    self.rotateServo(i)

            except KeyboardInterrupt:
                self.board.shutdown()
                sys.exit()

    def the_callback(self, data):
        self.distance = data[2]

    def capturaSensor(self):
        while(self.distance <= 120):
                time.sleep(2)
                self.board.sonar_read(self.triggerPin)

        if(self.distance > 120):
            return True