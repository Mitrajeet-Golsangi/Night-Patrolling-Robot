from pymata4 import pymata4
import time
import sys

# MIC_LEFT = 8
# MIC_RIGHT = 9
# board = pymata4.Pymata4()

# board.set_pin_mode_digital_input(MIC_LEFT)

# while True:
#     try:
#         data = board.digital_read(MIC_LEFT)[0]
#         print(data)
#         time.sleep(0.5)
#     except KeyboardInterrupt:
#         board.shutdown()
#         sys.exit(0)

lastEvent = 0
MIC_LEFT = 8
MIC_RIGHT = 9
MIC_FWD = 10
MIC_BWD = 11
board = pymata4.Pymata4()

board.set_pin_mode_digital_input(MIC_LEFT)
board.set_pin_mode_digital_input(MIC_RIGHT)
board.set_pin_mode_digital_input(MIC_FWD)
board.set_pin_mode_digital_input(MIC_BWD)


while True:
    try:
        sl = board.digital_read(MIC_LEFT)    
        sr = board.digital_read(MIC_RIGHT)
        sf = board.digital_read(MIC_FWD)
        sb = board.digital_read(MIC_BWD)
        vl = sl[0]
        vr = sr[0]
        vf = sf[0]
        vb = sb[0]
        print(vl,vr,vf,vb)
    except KeyboardInterrupt:
        board.shutdown()
        sys.exit(0)