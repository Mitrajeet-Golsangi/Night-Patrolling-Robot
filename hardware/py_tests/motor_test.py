import sys
import time

from pymata4 import pymata4

M1 = 4
M2 = 5
M3 = 6
M4 = 7

def motor(arduino):
   arduino.set_pin_mode_digital_output(M1)
   arduino.set_pin_mode_digital_output(M2)
   arduino.set_pin_mode_digital_output(M3)
   arduino.set_pin_mode_digital_output(M4)
   
   while True:
       try:
           arduino.digital_write(M1, 1)
           arduino.digital_write(M2, 0)
           arduino.digital_write(M3, 0)
           arduino.digital_write(M4, 1)
           time.sleep(0.5)
           arduino.digital_write(M1, 0)
           arduino.digital_write(M2, 1)
           arduino.digital_write(M3, 1)
           arduino.digital_write(M4, 0)
           time.sleep(0.5)
           
       except KeyboardInterrupt:
           arduino.shutdown()
           sys.exit(0)
 
board = pymata4.Pymata4()

try:
    motor(board)
    board.shutdown()    
except KeyboardInterrupt:
    board.shutdown()    
    sys.exit(0)
