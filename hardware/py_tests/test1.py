from pymata4 import pymata4
import time
import sys
from Main.hardware.py_tests.sound import MIC_BWD, MIC_FWD, MIC_LEFT, MIC_RIGHT

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

    board.set_pin_mode_digital_input(MIC_LEFT)
    board.set_pin_mode_digital_input(MIC_RIGHT)
    board.set_pin_mode_digital_input(MIC_FWD)
    board.set_pin_mode_digital_input(MIC_BWD)
    
    
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
    
    def get_mic_data(self):
        while True:
            try:
                sl = self.board.digital_read(MIC_LEFT)    
                sr = self.board.digital_read(MIC_RIGHT)
                sf = self.board.digital_read(MIC_FWD)
                sb = self.board.digital_read(MIC_BWD)
                vl = sl[0]
                vr = sr[0]
                vf = sf[0]
                vb = sb[0]
                return(vl,vr,vf,vb)
                # print(vl,vr,vf,vb)
            except KeyboardInterrupt:
                self.board.shutdown()
                sys.exit(0)
                
    def obs_det(self):
        cmp = HardwareComponents()
        obs_det = cmp.get_ultrasound_data()
        while True:
            try:
                if(obs_det<10):
                    cmp.motor_right_bwd()
            except KeyboardInterrupt:
                self.board.shutdown()
                sys.exit(0)
        
    def destroy(self):
        self.board.shutdown()
        
threshold = 160  

def main():
    cmp = HardwareComponents()

    lfm = cmp.get_mic_data('lf')
    lbm = cmp.get_mic_data('lb')
    rfm = cmp.get_mic_data('rf')
    rbm = cmp.get_mic_data('rb')
    
    obs_det() 
           
    if (vl is 0 and sound.vr is 1 and sound.vf is 0 and sound.vb is 1):
        cmp.motor_left_fwd()
        time.sleep(.5)

    elif (vl is 0 and sound.vr is 1 and sound.vf is 1 and sound.vb is 0):
        cmp.motor_left_bwd()
        time.sleep(.5)

    elif (sound.vl is 1 and sound.vr is 0 and sound.vf is 0 and sound.vb is 1):
        cmp.motor_right_fwd()
        time.sleep(.5)
        
    
    elif (sound.vl is 1 and sound.vr is 0 and sound.vf is 1 and sound.vb is 0):
        cmp.motor_right_bwd()
        time.sleep(.5)
        
    elif (sound.vl is 0 and sound.vr is 0 and sound.vf is 0 and sound.vb is 0):
        print("Sound detected from multiple directions")
        
    else :
        print("No sound percieved")
        
    
if __name__ == '__main__':
    main()


    # def get_mic_data(self, pos = 'lf'):
    #     if pos == 'lf':
    #         return self.board.digital_read(self.MIC_LEFT)
    #         return self.board.digital_read(self.MIC_FWD)        
    #     else:
    #         return self.board.digital_read(self.MIC_RIGHT)
    #         return self.board.digital_read(self.MIC_BWD)
    
    # def get_mic_data(self, pos = 'lb'):
    #     if pos == 'lb':
    #         return self.board.digital_read(self.MIC_LEFT)
    #         return self.board.digital_read(self.MIC_BWD)
    #     else:
    #         return self.board.digital_read(self.MIC_RIGHT)
    #         return self.board.digital_read(self.MIC_FWD)
    
    # def get_mic_data(self, pos = 'rf'):
    #     if pos == 'rf':
    #         return self.board.digital_read(self.MIC_RIGHT)
    #         return self.board.digital_read(self.MIC_FWD)
    #     else:
    #         return self.board.digital_read(self.MIC_LEFT)
    #         return self.board.digital_read(self.MIC_BWD)
    
    # def get_mic_data(self, pos = 'rb'):
    #     if pos == 'rb':
    #         return self.board.digital_read(self.MIC_RIGHT)
    #         return self.board.digital_read(self.MIC_BWD)
    #     else:
    #         return self.board.digital_read(self.MIC_LEFT)
    #         return self.board.digital_read(self.MIC_FWD)
    
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
    