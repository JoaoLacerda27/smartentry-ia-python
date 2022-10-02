import time
from pymata4 import pymata4

triggerPin = 11
echoPin = 12

board = pymata4.Pymata4()


def the_callback(data):
    print("distance: ", {data[2]})

board.set_pin_mode_sonar(triggerPin, echoPin, the_callback)

while True:
    try:
        time.sleep(2)
        board.sonar_read(triggerPin)
    except Exception:
        board.shutdown()