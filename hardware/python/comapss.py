import sys
import time
from telemetrix import telemetrix as tl


# the call back function to print the adxl345 data
def the_callback(data):
    print(data)


def adxl345(my_board):
    # setup adxl345
    ADDR = int(0x1E)
    X_LSB = int(0x03)
    my_board.set_pin_mode_i2c()

    # set up power and control register
    my_board.i2c_write(ADDR, [45, 0])
    time.sleep(.1)
    my_board.i2c_write(ADDR, [45, 8])
    time.sleep(.1)

    # set up the data format register
    my_board.i2c_write(ADDR, [49, 8])
    time.sleep(.1)
    my_board.i2c_write(ADDR, [49, 3])
    time.sleep(1)

    read_count = 20
    while True:
        # read 6 bytes from the data register
        my_board.i2c_read(ADDR, 50, 6, the_callback)
        try:
            time.sleep(.2)
            read_count -= 1
            if not read_count:
                print(f'reading: {my_board.i2c_read(ADDR)}')
                read_count = 20
        except KeyboardInterrupt:
            my_board.shutdown()
            sys.exit(0)


board = tl.Telemetrix()

try:
    adxl345(board)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)