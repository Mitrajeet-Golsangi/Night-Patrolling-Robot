from pymata4 import pymata4
import time
import sys

class HardwareComponents:
    board = pymata4.Pymata4()
    
    LEFT_MOTOR = (4, 5)
    RIGHT_MOTOR = (6, 7)

    ULTRASOUND_TRIG = 3
    ULTRASOUND_ECHO = 2

    MIC_LEFT = 8
    MIC_RIGHT = 9
    MIC_FWD = 10
    MIC_BWD = 11

    def _init_(self, *args, **kwargs):
        pymata4.set_pin_mode_digital_output(self.LEFT_MOTOR[0])
        pymata4.set_pin_mode_digital_output(self.LEFT_MOTOR[1])
        pymata4.set_pin_mode_digital_output(self.RIGHT_MOTOR[0])
        pymata4.set_pin_mode_digital_output(self.RIGHT_MOTOR[1])
        
        pymata4.set_pin_mode_digital_input(self.MIC_LEFT)
        pymata4.set_pin_mode_digital_input(self.MIC_RIGHT)

        pymata4.set_pin_mode_sonar(self.ULTRASOUND_TRIG, self.ULTRASOUND_ECHO)

    def motor_left_fwd(self):
        self.board.digital_write(self.LEFT_MOTOR[0], 1)
        self.board.digital_write(self.LEFT_MOTOR[1], 0)
    
    def motor_right_fwd(self):
        self.board.digital_write(self.RIGHT_MOTOR[0], 1)
        self.board.digital_write(self.RIGHT_MOTOR[1], 0)
    
    def motor_left_bwd(self):
        self.board.digital_write(self.LEFT_MOTOR[0], 0)
        self.board.digital_write(self.LEFT_MOTOR[1], 1)
    
    def motor_right_bwd(self):
        self.board.digital_write(self.RIGHT_MOTOR[0], 0)
        self.board.digital_write(self.RIGHT_MOTOR[1], 1)
    
    def get_ultrasound_data(self):
        return self.board.sonar_read(self.ULTRASOUND_TRIG)
    
    def get_mic_data(self, pos = 'lf'):
        if pos == 'lf':
            return self.board.digital_read(self.MIC_LEFT)
            return self.board.digital_read(self.MIC_FWD)
        else:
            return self.board.digital_read(self.MIC_RIGHT)
            return self.board.digital_read(self.MIC_BWD)
    
    def get_mic_data(self, pos = 'lb'):
        if pos == 'lb':
            return self.board.digital_read(self.MIC_LEFT)
            return self.board.digital_read(self.MIC_BWD)
        else:
            return self.board.digital_read(self.MIC_RIGHT)
            return self.board.digital_read(self.MIC_FWD)
    
    def get_mic_data(self, pos = 'rf'):
        if pos == 'rf':
            return self.board.digital_read(self.MIC_RIGHT)
            return self.board.digital_read(self.MIC_FWD)
        else:
            return self.board.digital_read(self.MIC_LEFT)
            return self.board.digital_read(self.MIC_BWD)
    
    def get_mic_data(self, pos = 'rb'):
        if pos == 'rb':
            return self.board.digital_read(self.MIC_RIGHT)
            return self.board.digital_read(self.MIC_BWD)
        else:
            return self.board.digital_read(self.MIC_LEFT)
            return self.board.digital_read(self.MIC_FWD)
    
    def destroy(self):
        self.board.shutdown()
        
threshold = 160  

def main():
    cmp = HardwareComponents()
    # while True:
    #     try:
    #         lfm = cmp.get_mic_data('lf')
    #         print(lfm)
    #         cmp.motor_left_fwd()
    #         time.sleep(.5)
            
    #         lbm = cmp.get_mic_data('lb')
    #         cmp.motor_left_bwd()
    #         time.sleep(.5)
            
    #         rfm = cmp.get_mic_data('rf')
    #         cmp.motor_right_fwd()
    #         time.sleep(.5)
            
    #         rbm = cmp.get_mic_data('rb')
    #         cmp.motor_right_bwd()
    #         time.sleep(.5)
            
    #     except KeyboardInterrupt:
    #         cmp.destroy()
    #         sys.exit(0)
    lfm = cmp.get_mic_data('lf')
    lbm = cmp.get_mic_data('lb')
    rfm = cmp.get_mic_data('rf')
    rbm = cmp.get_mic_data('rb')
    # if (lfm) :
    #     cmp.motor_left_fwd()
    #     time.sleep(.5)

    # elif (lbm) :
    #     cmp.motor_left_bwd()
    #     time.sleep(.5)

    if (rfm) :
        cmp.motor_right_fwd()
        time.sleep(.5)
        
    
    # elif (rbm) :
    #     cmp.motor_right_bwd()
    #     time.sleep(.5)
        
    else :
        print("No sound percieved")
        
    
if __name__ == '__main__':
    main()
