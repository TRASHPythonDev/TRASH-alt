from trash.movement_arduino import BoardManager
from pymata4 import pymata4
from time import perf_counter
from time import sleep



testBoard2 = BoardManager(1)
try:
    testBoard2.activate_pins_for_output([22,2]) # should work on most arduino boards
    testBoard2.set_stepper_direction(22, 0)
except:
    print("init failed")
    pass

x = 0
i = 0
rate = 0.0001
time_of_last = perf_counter()
while (x < 400):
        
    if(perf_counter() - time_of_last > rate):
        time_of_last = perf_counter()
        i = ~i
        testBoard2.step(2)
        x = x + 1     
    pass
testBoard2.delete_manager()
""""
def func(board):
    board.set_pin_mode_digital_output(22)

board = pymata4.Pymata4(arduino_instance_id = 1)
try:
    func(board)
    board.digital_write(22, 1)
    time.sleep(5)
    board.shutdown()
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
"""