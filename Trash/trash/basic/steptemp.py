import sys
import time
from pymata4 import pymata4

my_board = pymata4.Pymata4()
my_board.set_pin_mode_digital_output(2)
my_board.set_pin_mode_digital_output(3)
my_board.set_pin_mode_digital_output(4)
my_board.set_pin_mode_digital_output(5)
my_board.set_pin_mode_digital_output(6)
my_board.set_pin_mode_digital_output(7)
my_board.set_pin_mode_digital_output(8)
my_board.set_pin_mode_digital_output(22)
my_board.set_pin_mode_digital_output(23)
my_board.set_pin_mode_digital_output(24)
my_board.set_pin_mode_digital_output(25)
my_board.set_pin_mode_digital_output(26)
my_board.set_pin_mode_digital_output(27)
my_board.set_pin_mode_digital_output(28)

    #Rotation Direction
my_board.digital_write(22, 1)
my_board.digital_write(23, 1)
my_board.digital_write(24, 1)
my_board.digital_write(25, 1)
my_board.digital_write(26, 1)
my_board.digital_write(27, 1)
my_board.digital_write(28, 1)

 
mytime = -100

x = 0

while (x < 400):
        
    if (mytime < time.time()-.005):

        my_board.digital_write(2, 0)
        my_board.digital_write(3, 0)
        my_board.digital_write(4, 0)
        my_board.digital_write(5, 0)
        my_board.digital_write(6, 0)
        my_board.digital_write(7, 0)
        my_board.digital_write(8, 0) 

        my_board.digital_write(2, 1)
        my_board.digital_write(3, 1)
        my_board.digital_write(4, 1)
        my_board.digital_write(5, 1)
        my_board.digital_write(6, 1)
        my_board.digital_write(7, 1)
        my_board.digital_write(8, 1)

        mytime=time.time()
        x= x+1    

try:
    my_board.shutdown()
except KeyboardInterrupt:
    my_board.shutdown()
    sys.exit(0)