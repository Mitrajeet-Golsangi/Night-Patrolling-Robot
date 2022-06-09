import sys
import time
from pymata4 import pymata4

"""
This program continuously monitors an HC-SR04 Ultrasonic Sensor
It reports changes to the distance sensed.
"""
# indices into callback data
DISTANCE_CM = 2
TRIGGER_PIN = 3
ECHO_PIN = 2


# A callback function to display the distance
def the_callback(data):
    print(f'Distance in cm: {data[DISTANCE_CM]}')


def sonar(my_board, trigger_pin, echo_pin, callback):
    my_board.set_pin_mode_sonar(trigger_pin, echo_pin, callback)

    while True:
        try:
            time.sleep(1)
            print(f'data read: {my_board.sonar_read(TRIGGER_PIN)}')
        except KeyboardInterrupt:
            my_board.shutdown()
            sys.exit(0)


board = pymata4.Pymata4()

try:
    sonar(board, TRIGGER_PIN, ECHO_PIN, the_callback)
    board.shutdown()
except (KeyboardInterrupt, RuntimeError):
    board.shutdown()
    sys.exit(0)