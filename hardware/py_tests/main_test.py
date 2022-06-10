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

    board.set_pin_mode_digital_input(MIC_LEFT)
    board.set_pin_mode_digital_input(MIC_RIGHT)
    board.set_pin_mode_digital_input(MIC_FWD)
    board.set_pin_mode_digital_input(MIC_BWD)

    def _init_(self, *args, **kwargs):
        pymata4.set_pin_mode_digital_output(self.LEFT_MOTOR[0])
        pymata4.set_pin_mode_digital_output(self.LEFT_MOTOR[1])
        pymata4.set_pin_mode_digital_output(self.RIGHT_MOTOR[0])
        pymata4.set_pin_mode_digital_output(self.RIGHT_MOTOR[1])

    def get_ultrasound_data(self):
        return self.board.sonar_read(self.ULTRASOUND_TRIG)
        
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

    def get_left_mic_data(self):
        sl = self.board.digital_read(self.MIC_LEFT)
        vl = sl[0]
        return(vl)
        
    def get_right_mic_data(self):
        sr = self.board.digital_read(self.MIC_RIGHT)
        vr = sr[0]
        return(vr)
        
    def get_front_mic_data(self):
        sf = self.board.digital_read(self.MIC_FWD)
        vf = sf[0]
        return(vf)
        
    def get_back_mic_data(self):
        sb = self.board.digital_read(self.MIC_BWD)
        vb = sb[0]
        return(vb)
    
    def obs_det(self):
        comp = HardwareComponents()
        obs_det = comp.get_ultrasound_data()
        if(obs_det<10):
            comp.motor_right_bwd()


def main():
        
        comp = HardwareComponents()

        lm = comp.get_left_mic_data()
        rm = comp.get_right_mic_data()
        fm = comp.get_front_mic_data()
        bm = comp.get_back_mic_data()
        
        
        while True:
            try:
                
                comp.obs_det()
                
                if (lm is 0 and rm is 1 and fm is 0 and bm is 1):
                    comp.motor_left_fwd()
                    time.sleep(0.5)
                    
                elif (lm is 0 and rm is 1 and fm is 1 and bm is 0):
                    comp.motor_left_bwd()
                    time.sleep(0.5)
                    
                elif (lm is 1 and rm is 0 and fm is 0 and bm is 1):
                    comp.motor_right_fwd()
                    time.sleep(0.5)
                    
                elif (lm is 1 and rm is 1 and fm is 1 and bm is 0):
                    comp.motor_right_bwd()
                    time.sleep(0.5)
                    
                elif (lm is 0 and rm is 0 and fm is 0 and bm is 0):
                    print("Sound detected from multiple directions")
                    time.sleep(0.5)
                    
                elif (lm is 1 and rm is 1 and fm is 1 and bm is 1):
                    print("No sound detected")
                    time.sleep(0.5)
                    
                else:
                    time.sleep(0.5)
                    
            except KeyboardInterrupt:
                comp.board.shutdown()
                sys.exit(0)
                
if __name__ == '__main_test__':
    main()

                    
            
                
    

    
