import sys
import time
from pymata4 import pymata4
# from Main.hardware.py_tests.sonar_test import DISTANCE_CM
import sonar_test
from motor_test import motor


# def main(arduino):
#     motor(arduino)
#     # sonar_test.sonar(sonar_test.my_board, sonar_test.trigger_pin, sonar_test.echo_pin, sonar_test.callback) 
    # while True:
        
            
    #     try:
    #          if ({data[sonar_test.DISTANCE_CM]}>30):
                 
                 
    #          elif( {data[sonar_test.DISTANCE_CM]}<=30):
    #             arduino.digital_write(M1, 1)
    #             arduino.digital_write(M2, 0)
    #             arduino.digital_write(M3, 0)
    #             arduino.digital_write(M4, 1)
    #             time.sleep(0.5)
                
    #     except KeyboardInterrupt:
    #        arduino.shutdown()
    #        sys.exit(0)
            
    
    # print("Run successful")

motor()